from collections.abc import Iterator
from urllib.parse import urlparse, urlencode, urlunparse

from bigc._client import BigCommerceV3APIClient


class BigCommerceProductsAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self, *, include_variants: bool = False, include_custom_fields: bool = False) -> Iterator[dict]:
        """Return an iterator for all products"""
        url_parts = urlparse('/catalog/products')

        include = []
        if include_variants:
            include.append('variants')
        if include_custom_fields:
            include.append('custom_fields')

        query_dict = {}
        if include:
            query_dict['include'] = ','.join(include)
        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._v3_client.paginated_request('GET', urlunparse(url_parts))

    def get(self, product_id: int, *, include_variants: bool = False, include_custom_fields: bool = False) -> dict:
        """Get a specific product by its ID"""
        url_parts = urlparse(f'/catalog/products/{product_id}')

        include = []
        if include_variants:
            include.append('variants')
        if include_custom_fields:
            include.append('custom_fields')

        query_dict = {}
        if include:
            query_dict['include'] = ','.join(include)
        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._v3_client.request('GET', urlunparse(url_parts))
