from typing import Union
from uuid import UUID

from bigc._client import BigCommerceV3APIClient

UUIDLike = Union[UUID, str]


class BigCommerceCartsAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def get(self, cart_id: UUIDLike) -> dict:
        """Get a specific cart by its ID"""
        return self._v3_client.request('GET', f'/carts/{cart_id}')

    def create(self, line_items: list, **kwargs) -> dict:
        """Create a new cart"""
        payload = {'line_items': line_items, **kwargs}
        return self._v3_client.request('POST', '/carts', json=payload)

    def update(self, cart_id: UUIDLike, customer_id: int) -> dict:
        """Update a specific cart by its ID"""
        payload = {'customer_id': customer_id}
        return self._v3_client.request('PUT', f'/carts/{cart_id}', json=payload)

    def delete(self, cart_id: UUIDLike) -> None:
        """Delete a specific cart by its ID"""
        self._v3_client.request('DELETE', f'/carts/{cart_id}')

    def add_line_items(self, cart_id: UUIDLike, **kwargs) -> dict:
        """Add line items to a cart"""
        return self._v3_client.request('POST', f'/carts/{cart_id}/items', json=kwargs)

    def update_line_item(self, cart_id: UUIDLike, item_id: UUIDLike, **kwargs) -> dict:
        """Update a single line item in a cart"""
        return self._v3_client.request('PUT', f'/carts/{cart_id}/items/{item_id}', json=kwargs)

    def delete_line_item(self, cart_id: UUIDLike, item_id: UUIDLike) -> dict:
        """Remove a line item from a cart"""
        return self._v3_client.request('DELETE', f'/carts/{cart_id}/items/{item_id}')

    def create_redirect_url(self, cart_id: UUIDLike) -> dict:
        """Create a redirect URL for a cart"""
        return self._v3_client.request('POST', f'/carts/{cart_id}/redirect_urls')
