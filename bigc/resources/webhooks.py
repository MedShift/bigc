from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceWebhooksAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all webhooks"""

        return self._api.v3.get_many('/hooks', params=params, timeout=timeout)

    def get(self, webhook_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific webhook by its ID"""

        return self._api.v3.get(f'/hooks/{webhook_id}', timeout=timeout)

    def create(self, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Create a webhook under a specific scope"""

        return self._api.v3.post('/hooks', data=data, params=params, timeout=timeout)

    def update(self, webhook_id: int, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific webhook by its ID"""

        return self._api.v3.put(f'/hooks/{webhook_id}', data=data, params=params, timeout=timeout)

    def delete(self, webhook_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific webhook by its ID"""

        return self._api.v3.delete(f'/hooks/{webhook_id}', timeout=timeout)
