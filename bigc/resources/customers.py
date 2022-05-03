from collections.abc import Iterator
from typing import Any, Iterable
from urllib.parse import urlparse, urlencode, urlunparse

from bigc._client import BigCommerceV3APIClient
from bigc.exceptions import ResourceNotFoundError


class BigCommerceCustomersAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self, *, id_in: Iterable[int] = None, include_formfields: bool = False) -> Iterator[dict]:
        """Return an iterator for all customers"""
        url_parts = urlparse('/customers')

        query_dict = {}
        if id_in is not None:
            query_dict['id:in'] = ','.join(map(str, id_in))
        if include_formfields:
            query_dict['include'] = 'formfields'
        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._v3_client.paginated_request('GET', urlunparse(url_parts))

    def get(self, customer_id: int, *, include_formfields: bool = False) -> dict:
        """Get a specific customer by its ID"""
        url_parts = urlparse('/customers')

        query_dict = {'id:in': customer_id}
        if include_formfields:
            query_dict['include'] = 'formfields'
        url_parts = url_parts._replace(query=urlencode(query_dict))

        try:
            return self._v3_client.request('GET', urlunparse(url_parts))[0]
        except IndexError:
            raise ResourceNotFoundError()

    def update_form_field(self, customer_id: int, field_name: str, value: Any) -> dict:
        """Update a form field value for a single customer"""
        payload = [{
            'customer_id': customer_id,
            'name': field_name,
            'value': value,
        }]
        return self._v3_client.request('PUT', '/customers/form-field-values', json=payload)[0]
