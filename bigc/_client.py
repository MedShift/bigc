import itertools
from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import NoReturn
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

import requests

from bigc import exceptions

MAX_V2_PAGE_SIZE = 250
MAX_V3_PAGE_SIZE = 250


class BigCommerceRequestClient(ABC):
    def __init__(self, store_hash: str, access_token: str):
        self.store_hash = store_hash
        self.access_token = access_token

    def request(self, method: str, path: str, **kwargs):
        kwargs['headers'] = self._get_standard_request_headers() | kwargs.get('headers', {})

        try:
            response = requests.request(method, self._prepare_url(path), **kwargs)
        except requests.Timeout as exc:
            raise exceptions.BigCommerceServerError('Request timed out') from exc

        if response.ok:
            # Return None for empty responses instead of raising
            return response.json() if response.text else None
        else:
            self._handle_error(response)

    @abstractmethod
    def paginated_request(self, method: str, path: str, **kwargs) -> Generator:
        pass

    @abstractmethod
    def _prepare_url(self, path: str) -> str:
        pass

    def _get_standard_request_headers(self) -> dict:
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Auth-Token': self.access_token,
        }

    @staticmethod
    def _handle_error(response: requests.Response) -> NoReturn:
        # TODO: Try to extract an error message from the response body

        if response.status_code == 400:
            raise exceptions.BadRequestError()
        if response.status_code == 401:
            raise exceptions.InvalidAuthorizationError()
        if response.status_code == 403:
            raise exceptions.InsufficientScopesError()
        if response.status_code == 404:
            raise exceptions.ResourceNotFoundError()
        if response.status_code == 429:
            raise exceptions.RateLimitExceededError()
        if response.status_code == 500:
            raise exceptions.InternalBigCommerceError()
        if response.status_code == 503:
            raise exceptions.StoreUnavailableError()
        if response.status_code == 507:
            raise exceptions.PlanLimitExceededError()

        if 300 <= response.status_code < 400:
            raise exceptions.BigCommerceRedirectionError()
        if 400 <= response.status_code < 500:
            raise exceptions.BigCommerceClientError()
        if 500 <= response.status_code < 600:
            raise exceptions.BigCommerceServerError()

        raise exceptions.BigCommerceAPIException(f'Unexpected status code ({response.status_code})')


class BigCommerceV2APIClient(BigCommerceRequestClient):
    def _prepare_url(self, path: str) -> str:
        return f"https://api.bigcommerce.com/stores/{self.store_hash}/v2/{path.lstrip('/')}"

    def paginated_request(self, method: str, path: str, **kwargs) -> Generator:
        url_parts = urlparse(path)
        query_dict = parse_qs(url_parts.query)

        if 'limit' in query_dict or 'page' in query_dict:
            raise ValueError('path already has pagination query params')

        query_dict['limit'] = [str(MAX_V2_PAGE_SIZE)]

        for cur_page in itertools.count(1):
            query_dict['page'] = [str(cur_page)]
            paged_url_parts = url_parts._replace(query=urlencode(query_dict, doseq=True))

            res_data = super().request(method, urlunparse(paged_url_parts), **kwargs)

            # The API returns HTTP 204 (empty) past the last page
            if res_data is None:
                return

            if not isinstance(res_data, list):
                raise TypeError(f'expected list, got {type(res_data).__name__}')

            yield from res_data

            # Check if we're on the last page
            if len(res_data) < MAX_V2_PAGE_SIZE:
                return


class BigCommerceV3APIClient(BigCommerceRequestClient):
    def _prepare_url(self, path: str) -> str:
        return f"https://api.bigcommerce.com/stores/{self.store_hash}/v3/{path.lstrip('/')}"

    def request(self, method: str, path: str, **kwargs):
        # v3 response bodies are boxed in the 'data' key
        response = super().request(method, path, **kwargs)
        return None if response is None else response['data']

    def paginated_request(self, method: str, path: str, **kwargs) -> Generator:
        url_parts = urlparse(path)
        query_dict = parse_qs(url_parts.query)

        if 'limit' in query_dict or 'page' in query_dict:
            raise ValueError('path already has pagination query params')

        query_dict['limit'] = [str(MAX_V3_PAGE_SIZE)]

        cur_page = 1
        num_pages = 1  # Will be set to the right value in the loop
        while cur_page <= num_pages:
            query_dict['page'] = [str(cur_page)]
            paged_url_parts = url_parts._replace(query=urlencode(query_dict, doseq=True))

            res_data = super().request(method, urlunparse(paged_url_parts), **kwargs)

            cur_page += 1
            num_pages = int(res_data['meta']['pagination']['total_pages'])

            if not isinstance(res_data['data'], list):
                raise TypeError(f"expected list, got {type(res_data['data']).__name__}")

            yield from res_data['data']
