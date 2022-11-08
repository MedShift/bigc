from collections.abc import Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCategoriesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self) -> Iterator[dict]:
        """Return an iterator for all categories"""
        return self._api.v3.get_many('/catalog/categories')

    def get(self, category_id: int) -> dict:
        """Get a specific category by its ID"""
        return self._api.v3.get(f'/catalog/categories/{category_id}')

    def create(self, *, name: str, parent_id: int = 0, **kwargs) -> dict:
        """Create a category"""
        payload = {
            'name': name,
            'parent_id': parent_id,
            **kwargs
        }
        return self._api.v3.post('/catalog/categories', json=payload)

    def update(self, category_id: int, data: dict) -> dict:
        """Update a specific category by its ID"""
        return self._api.v3.put(f'/catalog/categories/{category_id}', json=data)

    def delete(self, category_id: int) -> dict:
        """Delete a specific category by its ID"""
        return self._api.v3.delete(f'/catalog/categories/{category_id}')
