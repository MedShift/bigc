from typing import Any, Iterator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceProductsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Iterator[dict[str, Any]]:
        """Return an iterator for all products"""

        return self._api.v3.get_many('/catalog/products', **kwargs)

    def get(self, product_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific product by its ID"""

        return self._api.v3.get(f'/catalog/products/{product_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a product"""

        return self._api.v3.post('/catalog/products', json=data, **kwargs)

    def update(self, product_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific product by its ID"""

        return self._api.v3.put(f'/catalog/products/{product_id}', json=data, **kwargs)

    def delete(self, product_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Delete a specific product by its ID"""
        return self._api.v3.delete(f'/catalog/products/{product_id}', **kwargs)

    def get_pricing(self, data: dict[str, Any], **kwargs) -> Iterator[dict[str, Any]]:
        """Return an iterator for batch product pricing"""
        return self._api.v3.post('/pricing/products', json=data, **kwargs)
