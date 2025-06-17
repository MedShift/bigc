from typing import Any, Generator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceWebhooksAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None,  None]:
        """Return an iterator for all webhooks"""

        return self._api.v3.get_many('/hooks', **kwargs)

    def get(self, webhook_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific webhook by its ID"""

        return self._api.v3.get(f'/hooks/{webhook_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a webhook under a specific scope"""

        return self._api.v3.post('/hooks', json=data, **kwargs)

    def update(self, webhook_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific webhook by its ID"""

        return self._api.v3.put(f'/hooks/{webhook_id}', json=data, **kwargs)

    def delete(self, webhook_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Delete a specific webhook by its ID"""

        return self._api.v3.delete(f'/hooks/{webhook_id}', **kwargs)
