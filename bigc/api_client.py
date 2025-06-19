import itertools
from abc import ABC, abstractmethod
from typing import Any, Iterator, NoReturn

import requests

from bigc.exceptions import BigCommerceException, BigCommerceNetworkError, GatewayTimeoutError

MAX_V2_PAGE_SIZE = 250
MAX_V3_PAGE_SIZE = 250


class BigCommerceRequestClient(ABC):
    def __init__(self, store_hash: str, access_token: str, timeout: float | None = None):
        self.store_hash = store_hash
        self.access_token = access_token
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        *,
        data: Any = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Make a request to the BigCommerce API (uses Requests internally)"""

        headers = self._get_standard_request_headers() | (headers or {})

        if timeout is None:
            timeout = self.timeout

        try:
            response = requests.request(
                method,
                self._prepare_url(path),
                data=data,
                params=self._process_params(params),
                headers=headers,
                timeout=timeout,
            )
        except requests.Timeout as exc:
            raise GatewayTimeoutError() from exc
        except requests.RequestException as exc:
            raise BigCommerceNetworkError() from exc

        if response.ok:
            # Return None for empty responses instead of raising
            return response.json() if response.text else None
        else:
            self._handle_error_response(response)

    def get(self, *args, **kwargs):
        """Alias for ``request('GET', ...)``"""
        return self.request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        """Alias for ``request('POST', ...)``"""
        return self.request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        """Alias for ``request('PUT', ...)``"""
        return self.request('PUT', *args, **kwargs)

    def delete(self, *args, **kwargs):
        """Alias for ``request('DELETE', ...)``"""
        return self.request('DELETE', *args, **kwargs)

    @abstractmethod
    def get_many(
        self,
        path: str,
        *,
        page_size: int | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Iterator[Any]:
        """Make a request to a paginated BigCommerce API endpoint"""
        pass

    @abstractmethod
    def _prepare_url(self, path: str) -> str:
        pass

    def _get_standard_request_headers(self) -> dict[str, str]:
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Auth-Token': self.access_token,
        }

    @staticmethod
    def _process_params(params: dict[str, Any] | None) -> dict[str, str] | None:
        if not params:
            return None

        def _process_param(value: Any) -> str:
            if isinstance(value, list | tuple | set):
                return ','.join(map(str, value))

            return str(value)

        return {k: _process_param(v) for k, v in params.items()}

    @staticmethod
    def _handle_error_response(response: requests.Response) -> NoReturn:
        try:
            message, errors = BigCommerceException.extract_error_message(response.json())
        except requests.JSONDecodeError:
            message, errors = None, None

        exc_class = BigCommerceException.get_exc_class_for_status_code(response.status_code)
        raise exc_class(
            message=message,
            status_code=response.status_code,
            response=response,
            errors=errors,
        )


class BigCommerceV2APIClient(BigCommerceRequestClient):
    """A client for directly calling BigCommerce v2 API endpoints"""

    def _prepare_url(self, path: str) -> str:
        return f"https://api.bigcommerce.com/stores/{self.store_hash}/v2/{path.lstrip('/')}"

    def get_many(
        self,
        path: str,
        *,
        page_size: int | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Iterator[Any]:
        page_size = MAX_V2_PAGE_SIZE if page_size is None else int(page_size)

        params = params or {}

        if 'limit' in params or 'page' in params:
            raise ValueError('path already has pagination query params')

        params['limit'] = page_size

        for cur_page in itertools.count(1):
            params['page'] = cur_page

            res_data = super().get(path, params=params, timeout=timeout)

            # The API returns HTTP 204 (empty) past the last page
            if res_data is None:
                return

            if not isinstance(res_data, list):
                raise TypeError(f'expected list, got {type(res_data).__name__}')

            yield from res_data

            # Check if we're on the last page
            if len(res_data) < page_size:
                return


class BigCommerceV3APIClient(BigCommerceRequestClient):
    """A client for directly calling BigCommerce v3 API endpoints"""

    def _prepare_url(self, path: str) -> str:
        return f"https://api.bigcommerce.com/stores/{self.store_hash}/v3/{path.lstrip('/')}"

    def request(self, *args, **kwargs):
        # v3 response bodies are boxed in the 'data' key
        response = super().request(*args, **kwargs)
        return None if response is None else response['data']

    def get_many(
        self,
        path: str,
        *,
        page_size: int | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Iterator[Any]:
        page_size = MAX_V3_PAGE_SIZE if page_size is None else int(page_size)

        params = params or {}

        if 'limit' in params or 'page' in params:
            raise ValueError('path already has pagination query params')

        params['limit'] = page_size

        cur_page = 1
        num_pages = 1  # Will be set to the right value in the loop
        while cur_page <= num_pages:
            params['page'] = cur_page

            res_data = super().request('GET', path, params=params, timeout=timeout)

            cur_page += 1
            num_pages = int(res_data['meta']['pagination']['total_pages'])

            if not isinstance(res_data['data'], list):
                raise TypeError(f"expected list, got {type(res_data['data']).__name__}")

            yield from res_data['data']


class BigCommerceAPIClient:
    def __init__(self, *args, **kwargs):
        self.v2: BigCommerceV2APIClient = BigCommerceV2APIClient(*args, **kwargs)
        self.v3: BigCommerceV3APIClient = BigCommerceV3APIClient(*args, **kwargs)
