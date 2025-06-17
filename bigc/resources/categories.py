from typing import Any, Generator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceCategoriesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None,  None]:
        """Return an iterator for all categories"""

        return self._api.v3.get_many('/catalog/categories', **kwargs)

    def get(self, category_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific category by its ID"""

        return self._api.v3.get(f'/catalog/categories/{category_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a category"""

        return self._api.v3.post('/catalog/categories', json=data, **kwargs)

    def update(self, category_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific category by its ID"""

        return self._api.v3.put(f'/catalog/categories/{category_id}', json=data, **kwargs)

    def delete(self, category_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Delete a specific category by its ID"""

        return self._api.v3.delete(f'/catalog/categories/{category_id}', **kwargs)
