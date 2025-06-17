from typing import TypeAlias, Unpack, Any, Union
from uuid import UUID

from bigc.api_client import BigCommerceAPIClient, RequestOptions

UUIDLike: TypeAlias = UUID | str


class BigCommerceCartsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def get(self, cart_id: UUIDLike, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific cart by its ID"""

        return self._api.v3.get(f'/carts/{cart_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a new cart"""

        return self._api.v3.post('/carts', json=data, **kwargs)

    def update(self, cart_id: UUIDLike, data: dict[str, Any]) -> dict[str, Any]:
        """Update a specific cart by its ID"""

        return self._api.v3.put(f'/carts/{cart_id}', json=data)

    def delete(self, cart_id: UUIDLike, **kwargs: Unpack[RequestOptions]) -> None:
        """Delete a specific cart by its ID"""

        self._api.v3.delete(f'/carts/{cart_id}', **kwargs)

    def add_line_items(self, cart_id: UUIDLike, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Add line items to a cart"""

        return self._api.v3.post(f'/carts/{cart_id}/items', json=data, **kwargs)

    def update_line_item(self, cart_id: UUIDLike, item_id: UUIDLike, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a single line item in a cart"""

        return self._api.v3.put(f'/carts/{cart_id}/items/{item_id}', json=data, **kwargs)

    def delete_line_item(self, cart_id: UUIDLike, item_id: UUIDLike, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Remove a line item from a cart"""

        return self._api.v3.delete(f'/carts/{cart_id}/items/{item_id}', **kwargs)

    def create_redirect_url(self, cart_id: UUIDLike, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a redirect URL for a cart"""

        return self._api.v3.post(f'/carts/{cart_id}/redirect_urls', **kwargs)
