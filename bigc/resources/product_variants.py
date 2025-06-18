from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceProductVariantsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, product_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all variants of a product"""

        return self._api.v3.get_many(f'/catalog/products/{product_id}/variants', params=params, timeout=timeout)

    def get(self, product_id: int, variant_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific product variant by ID"""

        return self._api.v3.get(f'/catalog/products/{product_id}/variants/{variant_id}', params=params, timeout=timeout)

    def create(self, product_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Create a product variant"""

        return self._api.v3.post(f'/catalog/products/{product_id}/variants', json=data, timeout=timeout)

    def update(self, product_id: int, variant_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific product variant by its ID"""

        return self._api.v3.put(f'/catalog/products/{product_id}/variants/{variant_id}', json=data, timeout=timeout)

    def delete(self, product_id: int, variant_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific product variant by its ID"""

        return self._api.v3.delete(f'/catalog/products/{product_id}/variants/{variant_id}', timeout=timeout)
