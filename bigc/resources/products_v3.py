from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceProductsV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all products"""
        return self._api.get_many('/catalog/products', params=params, timeout=timeout, retries=retries)

    def get(
            self,
            product_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific product by its ID"""
        return self._api.get(f'/catalog/products/{product_id}', params=params, timeout=timeout, retries=retries)

    def create(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a product"""
        return self._api.post('/catalog/products', data=data, params=params, timeout=timeout)

    def update(
            self,
            product_id: int,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific product by its ID"""
        return self._api.put(f'/catalog/products/{product_id}', data=data, params=params, timeout=timeout, retries=retries)

    def delete(self, product_id: int, *, timeout: float | None = None, retries: int | None = None) -> dict[str, Any]:
        """Delete a specific product by its ID"""
        return self._api.delete(f'/catalog/products/{product_id}', timeout=timeout, retries=retries)
