from typing import Any, Iterator

from bigc.exceptions import DoesNotExistError
from bigc.api_client import BigCommerceAPIClient


class BigCommerceOrdersAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all orders"""

        return self._api.v2.get_many('/orders', params=params, timeout=timeout)

    def get(self, order_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get an order by its ID"""

        return self._api.v2.get(f'/orders/{order_id}', params=params, timeout=timeout)

    def create(self, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Create an order"""

        return self._api.v2.post('/orders', data=data, params=params, timeout=timeout)

    def update(self, order_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific order by its ID"""

        return self._api.v2.put(f'/orders/{order_id}', data=data, timeout=timeout)

    def archive(self, order_id: int, *, timeout: float | None = None) -> None:
        """Archive a specific order by its ID"""

        self._api.v2.delete(f'/orders/{order_id}', timeout=timeout)

    def all_products(self, order_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all order products in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/products', params=params, timeout=timeout)

    def get_product(self, order_id: int, product_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific order product in an order by ID"""

        return self._api.v2.get(f'/orders/{order_id}/products/{product_id}', timeout=timeout)

    def get_refund_quote(self, order_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Get a refund quote for an order by ID"""

        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refund_quotes', data=data, timeout=timeout)

    def create_refund(self, order_id: int, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Create a refund for an order by ID"""

        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refunds', data=data, params=params, timeout=timeout)

    def all_refunds(self, order_id: int | None = None, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all refunds, optionally filtered by order"""

        if order_id:
            endpoint = f'/orders/{order_id}/payment_actions/refunds'
        else:
            endpoint = '/orders/payment_actions/refunds'

        return self._api.v3.get_many(endpoint, params=params, timeout=timeout)

    def get_refund(self, refund_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific refund by its ID"""

        params = {
            **(params or {}),
            'id:in': refund_id,
        }

        try:
            return self._api.v3.get('/orders/payment_actions/refunds', params=params, timeout=timeout)[0]
        except IndexError:
            raise DoesNotExistError() from None

    def all_shipping_addresses(self, order_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all order shipping addresses in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipping_addresses', params=params, timeout=timeout)

    def get_shipping_address(self, order_id: int, address_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific shipping address in an order by ID"""

        return self._api.v2.get(f'/orders/{order_id}/shipping_addresses/{address_id}', timeout=timeout)

    def update_shipping_address(self, order_id: int, address_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific shipping address in an order by ID"""

        return self._api.v2.put(f'/orders/{order_id}/shipping_addresses/{address_id}', data=data, timeout=timeout)

    def all_shipments(self, order_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Returns all shipments for a specified order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipments', params=params, timeout=timeout)

    def get_shipment(self, order_id: int, shipment_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Get a shipment by its ID"""

        return self._api.v2.get(f'/orders/{order_id}/shipments/{shipment_id}', timeout=timeout)

    def create_shipment(self, order_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Creates an order shipment for the specified order"""

        return self._api.v2.post(f'/orders/{order_id}/shipments', data=data, timeout=timeout)

    def update_shipment(self, order_id: int, shipment_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Updates an order shipment for the specified order"""

        return self._api.v2.put(f'/orders/{order_id}/shipments/{shipment_id}', data=data, timeout=timeout)

    def delete_shipment(self, order_id: int, shipment_id: int, *, timeout: float | None = None) -> None:
        """Deletes specific shipment by its ID"""

        return self._api.v2.delete(f'/orders/{order_id}/shipments/{shipment_id}', timeout=timeout)

    def all_coupons(self, order_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all coupons in an order"""

        return self._api.v2.get_many(f'/orders/{order_id}/coupons', params=params, timeout=timeout)
