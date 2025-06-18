from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceProductsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all products"""

        return self._api.v3.get_many('/catalog/products', params=params, timeout=timeout)

    def get(self, product_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific product by its ID"""

        return self._api.v3.get(f'/catalog/products/{product_id}', params=params, timeout=timeout)

    def create(self, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Create a product"""

        return self._api.v3.post('/catalog/products', json=data, params=params, timeout=timeout)

    def update(self, product_id: int, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific product by its ID"""

        return self._api.v3.put(f'/catalog/products/{product_id}', json=data, params=params, timeout=timeout)

    def delete(self, product_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific product by its ID"""

        return self._api.v3.delete(f'/catalog/products/{product_id}', timeout=timeout)

    def get_pricing(self, data: dict[str, Any], *, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for batch product pricing"""

        return self._api.v3.post('/pricing/products', json=data, timeout=timeout)
