from typing import Any, TypeAlias
from uuid import UUID

from bigc.api_client import BigCommerceAPIClient

UUIDLike: TypeAlias = UUID | str


class BigCommerceCartsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def get(
            self,
            cart_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Get a specific cart by its ID"""
        return self._api.v3.get(f'/carts/{cart_id}', params=params, timeout=timeout)

    def create(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a new cart"""
        return self._api.v3.post('/carts', data=data, params=params, timeout=timeout)

    def update(self, cart_id: UUIDLike, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific cart by its ID"""
        return self._api.v3.put(f'/carts/{cart_id}', data=data, timeout=timeout)

    def delete(self, cart_id: UUIDLike, *, timeout: float | None = None) -> None:
        """Delete a specific cart by its ID"""
        self._api.v3.delete(f'/carts/{cart_id}', timeout=timeout)

    def add_line_items(
            self,
            cart_id: UUIDLike,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Add line items to a cart"""
        return self._api.v3.post(f'/carts/{cart_id}/items', data=data, params=params, timeout=timeout)

    def update_line_item(
            self,
            cart_id: UUIDLike,
            item_id: UUIDLike,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Update a single line item in a cart"""
        return self._api.v3.put(f'/carts/{cart_id}/items/{item_id}', data=data, params=params, timeout=timeout)

    def delete_line_item(
            self,
            cart_id: UUIDLike,
            item_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Remove a line item from a cart"""
        return self._api.v3.delete(f'/carts/{cart_id}/items/{item_id}', params=params, timeout=timeout)

    def create_redirect_url(
            self,
            cart_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a redirect URL for a cart"""
        return self._api.v3.post(f'/carts/{cart_id}/redirect_urls', params=params, timeout=timeout)
