from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCategoriesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all categories"""
        return self._api.v3.get_many('/catalog/categories', params=params, timeout=timeout)

    def get(self, category_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific category by its ID"""
        return self._api.v3.get(f'/catalog/categories/{category_id}', timeout=timeout)

    def create(self, data: dict[str, Any], timeout: float | None = None) -> dict[str, Any]:
        """Create a category"""
        return self._api.v3.post('/catalog/categories', data=data, timeout=timeout)

    def update(self, category_id: int, data: dict[str, Any], timeout: float | None = None) -> dict[str, Any]:
        """Update a specific category by its ID"""
        return self._api.v3.put(f'/catalog/categories/{category_id}', data=data, timeout=timeout)

    def delete(self, category_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific category by its ID"""
        return self._api.v3.delete(f'/catalog/categories/{category_id}', timeout=timeout)
