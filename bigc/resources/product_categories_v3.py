from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceProductCategoriesV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

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
