from collections.abc import Iterator

from bigc._client import BigCommerceV3APIClient


class BigCommerceCategoriesAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self) -> Iterator[dict]:
        """Return an iterator for all categories"""
        return self._v3_client.paginated_request('GET', '/catalog/categories')

    def get(self, category_id: int) -> dict:
        """Get a specific category by its ID"""
        return self._v3_client.request('GET', f'/catalog/categories/{category_id}')

    def create(self, *, name: str, parent_id: int = 0, **kwargs) -> dict:
        """Create a category"""
        payload = {
            'name': name,
            'parent_id': parent_id,
            **kwargs
        }
        return self._v3_client.request('POST', '/catalog/categories', json=payload)

    def update(self, category_id: int, data: dict) -> dict:
        """Update a specific category by its ID"""
        return self._v3_client.request('PUT', f'/catalog/categories/{category_id}', json=data)

    def delete(self, category_id: int) -> dict:
        """Delete a specific category by its ID"""
        return self._v3_client.request('DELETE', f'/catalog/categories/{category_id}')
