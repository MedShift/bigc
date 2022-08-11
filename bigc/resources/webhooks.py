from collections.abc import Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceWebhooksAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self) -> Iterator[dict]:
        """Return an iterator for all webhooks"""
        return self._api.v3.get_many('/hooks')

    def get(self, webhook_id: int) -> dict:
        """Get a specific webhook by its ID"""
        return self._api.v3.get(f'/hooks/{webhook_id}')

    def create(self, *, scope: str, destination: str, headers: dict, is_active: bool = True) -> dict:
        """Create a webhook under a specific scope"""
        payload = {
            'scope': scope,
            'destination': destination,
            'headers': headers,
            'is_active': is_active,
        }
        return self._api.v3.post('/hooks', json=payload)

    def update(self, webhook_id: int, data: dict) -> dict:
        """Update a specific webhook by its ID"""
        return self._api.v3.put(f'/hooks/{webhook_id}', json=data)

    def delete(self, webhook_id: int) -> dict:
        """Delete a specific webhook by its ID"""
        return self._api.v3.delete(f'/hooks/{webhook_id}')
