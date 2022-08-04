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

    def create(self, *, name: str, product_type: str, weight: float, price: float, **kwargs) -> dict:
        """Create a product"""
        payload = {
            'name': name,
            'type': product_type,
            'weight': weight,
            'price': price,
            **kwargs,
        }
        return self._v3_client.request('POST', '/catalog/products', json=payload)

    def update(self, product_id: int, data: dict) -> dict:
        """Update a specific product by its ID"""
        return self._v3_client.request('PUT', f'/catalog/products/{product_id}', json=data)

    def delete(self, product_id: int) -> dict:
        """Delete a specific product by its ID"""
        return self._v3_client.request('DELETE', f'/catalog/products/{product_id}')

    def get_pricing(self, items: list[dict], *, channel_id: int = 1, currency_code: str = 'USD',
                    customer_group_id: int = 0) -> Iterator[dict]:
        """Return an iterator for batch product pricing"""
        return self._v3_client.request('POST', '/pricing/products', json={
            'channel_id': channel_id,
            'currency_code': currency_code,
            'customer_group_id': customer_group_id,
            'items': list(items),
        })
