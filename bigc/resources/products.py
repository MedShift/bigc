from collections.abc import Iterator
from urllib.parse import urlencode, urlparse, urlunparse

from bigc.api_client import BigCommerceAPIClient


class BigCommerceProductsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

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

        return self._api.v3.get_many(urlunparse(url_parts))

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

        return self._api.v3.get(urlunparse(url_parts))

    def create(self, *, name: str, product_type: str, weight: float, price: float, **kwargs) -> dict:
        """Create a product"""
        payload = {
            'name': name,
            'type': product_type,
            'weight': weight,
            'price': price,
            **kwargs,
        }
        return self._api.v3.post('/catalog/products', json=payload)

    def update(self, product_id: int, data: dict) -> dict:
        """Update a specific product by its ID"""
        return self._api.v3.put(f'/catalog/products/{product_id}', json=data)

    def delete(self, product_id: int) -> dict:
        """Delete a specific product by its ID"""
        return self._api.v3.delete(f'/catalog/products/{product_id}')

    def get_pricing(self, items: list[dict], *, channel_id: int = 1, currency_code: str = 'USD',
                    customer_group_id: int = 0) -> Iterator[dict]:
        """Return an iterator for batch product pricing"""
        return self._api.v3.post('/pricing/products', json={
            'channel_id': channel_id,
            'currency_code': currency_code,
            'customer_group_id': customer_group_id,
            'items': list(items),
        })
