from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceProductVariantsV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all(
            self,
            product_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all variants of a product"""
        return self._api.get_many(f'/catalog/products/{product_id}/variants', params=params, timeout=timeout, retries=retries)

    def get(
            self,
            product_id: int,
            variant_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific product variant by ID"""
        return self._api.get(f'/catalog/products/{product_id}/variants/{variant_id}', params=params, timeout=timeout, retries=retries)

    def create(
            self,
            product_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a product variant"""
        return self._api.post(f'/catalog/products/{product_id}/variants', data=data, timeout=timeout)

    def update(
            self,
            product_id: int,
            variant_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific product variant by its ID"""
        return self._api.put(f'/catalog/products/{product_id}/variants/{variant_id}', data=data, timeout=timeout, retries=retries)

    def delete(
            self,
            product_id: int,
            variant_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Delete a specific product variant by its ID"""
        return self._api.delete(f'/catalog/products/{product_id}/variants/{variant_id}', timeout=timeout, retries=retries)
