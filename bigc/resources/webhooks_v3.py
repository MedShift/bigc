from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommerceWebhooksV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all webhooks"""
        return self._api.get_many('/hooks', params=params, timeout=timeout, retries=retries)

    def get(self, webhook_id: int, *, timeout: float | None = None, retries: int | None = None) -> dict[str, Any]:
        """Get a specific webhook by its ID"""
        return self._api.get(f'/hooks/{webhook_id}', timeout=timeout, retries=retries)

    def create(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a webhook under a specific scope"""
        return self._api.post('/hooks', data=data, params=params, timeout=timeout)

    def update(
            self,
            webhook_id: int,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific webhook by its ID"""
        return self._api.put(f'/hooks/{webhook_id}', data=data, params=params, timeout=timeout, retries=retries)

    def delete(self, webhook_id: int, *, timeout: float | None = None, retries: int | None = None) -> dict[str, Any]:
        """Delete a specific webhook by its ID"""
        return self._api.delete(f'/hooks/{webhook_id}', timeout=timeout, retries=retries)
