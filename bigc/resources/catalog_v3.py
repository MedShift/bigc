from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceCatalogV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all_products(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all products"""
        return self._api.get_many('/catalog/products', params=params, timeout=timeout)

    def get_product(
            self,
            product_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Get a specific product by its ID"""
        return self._api.get(f'/catalog/products/{product_id}', params=params, timeout=timeout)

    def create_product(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a product"""
        return self._api.post('/catalog/products', data=data, params=params, timeout=timeout)

    def update_product(
            self,
            product_id: int,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Update a specific product by its ID"""
        return self._api.put(f'/catalog/products/{product_id}', data=data, params=params, timeout=timeout)

    def delete_product(self, product_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific product by its ID"""
        return self._api.delete(f'/catalog/products/{product_id}', timeout=timeout)

    def all_product_variants(
            self,
            product_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all variants of a product"""
        return self._api.get_many(f'/catalog/products/{product_id}/variants', params=params, timeout=timeout)

    def get_product_variant(
            self,
            product_id: int,
            variant_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Get a specific product variant by ID"""
        return self._api.get(f'/catalog/products/{product_id}/variants/{variant_id}', params=params, timeout=timeout)

    def create_product_variant(
            self,
            product_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a product variant"""
        return self._api.post(f'/catalog/products/{product_id}/variants', data=data, timeout=timeout)

    def update_product_variant(
            self,
            product_id: int,
            variant_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Update a specific product variant by its ID"""
        return self._api.put(f'/catalog/products/{product_id}/variants/{variant_id}', data=data, timeout=timeout)

    def delete_product_variant(
            self,
            product_id: int,
            variant_id: int,
            *,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Delete a specific product variant by its ID"""
        return self._api.delete(f'/catalog/products/{product_id}/variants/{variant_id}', timeout=timeout)

    def all_categories(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all categories"""
        return self._api.get_many('/catalog/categories', params=params, timeout=timeout)

    def get_category(self, category_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific category by its ID"""
        return self._api.get(f'/catalog/categories/{category_id}', timeout=timeout)

    def create_category(self, data: dict[str, Any], timeout: float | None = None) -> dict[str, Any]:
        """Create a category"""
        return self._api.post('/catalog/categories', data=data, timeout=timeout)

    def update_category(self, category_id: int, data: dict[str, Any], timeout: float | None = None) -> dict[str, Any]:
        """Update a specific category by its ID"""
        return self._api.put(f'/catalog/categories/{category_id}', data=data, timeout=timeout)

    def delete_category(self, category_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific category by its ID"""
        return self._api.delete(f'/catalog/categories/{category_id}', timeout=timeout)
