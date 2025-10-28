from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceCategoriesV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all categories"""
        return self._api.get_many('/catalog/categories', params=params, timeout=timeout, retries=retries)

    def get(self, category_id: int, *, timeout: float | None = None, retries: int | None = None) -> dict[str, Any]:
        """Get a specific category by its ID"""
        return self._api.get(f'/catalog/categories/{category_id}', timeout=timeout, retries=retries)

    def create(self, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Create a category"""
        return self._api.post('/catalog/categories', data=data, timeout=timeout)

    def update(
            self,
            category_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific category by its ID"""
        return self._api.put(f'/catalog/categories/{category_id}', data=data, timeout=timeout, retries=retries)

    def delete(self, category_id: int, *, timeout: float | None = None, retries: int | None = None) -> dict[str, Any]:
        """Delete a specific category by its ID"""
        return self._api.delete(f'/catalog/categories/{category_id}', timeout=timeout, retries=retries)
