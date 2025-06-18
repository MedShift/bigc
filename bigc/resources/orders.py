from typing import Any, Generator, Unpack

from bigc.api_client import RequestOptions
from bigc.api_client import BigCommerceAPIClient
from bigc.exceptions import DoesNotExistError


class BigCommerceOrdersAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Return a generator for all orders"""

        return self._api.v2.get_many('/orders', page_size=5, **kwargs)

    def get(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get an order by its ID"""

        return self._api.v2.get(f'/orders/{order_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create an order"""

        return self._api.v2.post('/orders', json=data, **kwargs)

    def update(self, order_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific order by its ID"""

        return self._api.v2.put(f'/orders/{order_id}', json=data, **kwargs)

    def archive(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> None:
        """Archive a specific order by its ID"""

        self._api.v2.delete(f'/orders/{order_id}', **kwargs)

    def all_products(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Return a generator for all order products in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/products', **kwargs)

    def get_product(self, order_id: int, product_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific order product in an order by ID"""

        return self._api.v2.get(f'/orders/{order_id}/products/{product_id}', **kwargs)

    def get_refund_quote(self, order_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a refund quote for an order by ID"""

        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refund_quotes', json=data, **kwargs)

    def create_refund(self, order_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a refund for an order by ID"""

        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refunds', json=data, **kwargs)

    def all_refunds(self, order_id: int | None = None, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Return a generator for all refunds, optionally filtered by order"""

        if order_id:
            endpoint = f'/orders/{order_id}/payment_actions/refunds'
        else:
            endpoint = '/orders/payment_actions/refunds'

        return self._api.v3.get_many(endpoint, **kwargs)

    def get_refund(self, refund_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific refund by its ID"""

        kwargs['params'] = {
            **(kwargs.get('params') or {}),
            'id:in': refund_id,
        }

        try:
            return self._api.v3.get('/orders/payment_actions/refunds', **kwargs)[0]
        except IndexError:
            raise DoesNotExistError() from None

    def all_shipping_addresses(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Return a generator for all order shipping addresses in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipping_addresses', **kwargs)

    def get_shipping_address(self, order_id: int, address_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific shipping address in an order by ID"""

        return self._api.v2.get(f'/orders/{order_id}/shipping_addresses/{address_id}', **kwargs)

    def update_shipping_address(self, order_id: int, address_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific shipping address in an order by ID"""

        return self._api.v2.put(f'/orders/{order_id}/shipping_addresses/{address_id}', json=data, **kwargs)

    def all_shipments(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Returns all shipments for a specified order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipments', **kwargs)

    def get_shipment(self, order_id: int, shipment_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a shipment by its ID"""

        return self._api.v2.get(f'/orders/{order_id}/shipments/{shipment_id}', **kwargs)

    def create_shipment(self, order_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Creates an order shipment for the specified order"""

        return self._api.v2.post(f'/orders/{order_id}/shipments', json=data, **kwargs)

    def update_shipment(self, order_id: int, shipment_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Updates an order shipment for the specified order"""

        return self._api.v2.put(f'/orders/{order_id}/shipments/{shipment_id}', json=data, **kwargs)

    def delete_shipment(self, order_id: int, shipment_id: int, **kwargs: Unpack[RequestOptions]) -> None:
        """Deletes specific shipment by its ID"""

        return self._api.v2.delete(f'/orders/{order_id}/shipments/{shipment_id}', **kwargs)

    def all_coupons(self, order_id: int, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None, None]:
        """Return a generator for all coupons in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/coupons', **kwargs)
