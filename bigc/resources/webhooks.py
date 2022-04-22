from collections.abc import Iterator

from bigc._client import BigCommerceV3APIClient


class BigCommerceWebhooksAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self) -> Iterator[dict]:
        """Return an iterator for all webhooks"""
        return self._v3_client.paginated_request('GET', '/hooks')

    def get(self, webhook_id: int) -> dict:
        """Get a specific webhook by its ID"""
        return self._v3_client.request('GET', f'/hooks/{webhook_id}')

    def create(self, *, scope: str, destination: str, headers: dict, is_active: bool = True) -> dict:
        """Create a webhook under a specific scope"""
        payload = {
            'scope': scope,
            'destination': destination,
            'headers': headers,
            'is_active': is_active,
        }
        return self._v3_client.request('POST', '/hooks', json=payload)

    def update(self, webhook_id: int, data: dict) -> dict:
        """Update a specific webhook by its ID"""
        return self._v3_client.request('PUT', f'/hooks/{webhook_id}', json=data)

    def delete(self, webhook_id: int) -> dict:
        """Delete a specific webhook by its ID"""
        return self._v3_client.request('DELETE', f'/hooks/{webhook_id}')
