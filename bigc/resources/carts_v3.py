from typing import Any, TypeAlias
from uuid import UUID

from bigc.api_client import BigCommerceV3APIClient

UUIDLike: TypeAlias = UUID | str


class BigCommerceCartsV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def get(
            self,
            cart_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific cart by its ID"""
        return self._api.get(f'/carts/{cart_id}', params=params, timeout=timeout, retries=retries)

    def create(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a new cart"""
        return self._api.post('/carts', data=data, params=params, timeout=timeout)

    def update(
            self,
            cart_id: UUIDLike,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific cart by its ID"""
        return self._api.put(f'/carts/{cart_id}', data=data, params=params, timeout=timeout, retries=retries)

    def delete(self, cart_id: UUIDLike, *, timeout: float | None = None, retries: int | None = None) -> None:
        """Delete a specific cart by its ID"""
        self._api.delete(f'/carts/{cart_id}', timeout=timeout, retries=retries)

    def add_line_items(
            self,
            cart_id: UUIDLike,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Add line items to a cart"""
        return self._api.post(f'/carts/{cart_id}/items', data=data, params=params, timeout=timeout)

    def update_line_item(
            self,
            cart_id: UUIDLike,
            item_id: UUIDLike,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a single line item in a cart"""
        return self._api.put(f'/carts/{cart_id}/items/{item_id}', data=data, params=params, timeout=timeout, retries=retries)

    def delete_line_item(
            self,
            cart_id: UUIDLike,
            item_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Remove a line item from a cart"""
        return self._api.delete(f'/carts/{cart_id}/items/{item_id}', params=params, timeout=timeout, retries=retries)

    def create_redirect_url(
            self,
            cart_id: UUIDLike,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a redirect URL for a cart"""
        return self._api.post(f'/carts/{cart_id}/redirect_urls', params=params, timeout=timeout)
