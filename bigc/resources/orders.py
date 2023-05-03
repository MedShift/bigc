from collections.abc import Iterator
from typing import Optional
from urllib.parse import urlencode, urlparse, urlunparse

from bigc.api_client import BigCommerceAPIClient
from bigc.exceptions import ResourceNotFoundError


class BigCommerceOrdersAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, customer_id: Optional[int] = None) -> Iterator[dict]:
        """Return an iterator for all orders"""
        url_parts = urlparse('/orders')

        query_dict = {}
        if customer_id:
            query_dict['customer_id'] = str(customer_id)
        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._api.v2.get_many(urlunparse(url_parts))

    def get(self, order_id: int) -> dict:
        """Get an order by its ID"""
        return self._api.v2.get(f'/orders/{order_id}')

    def create(self, *, products: list[dict], billing_address: dict, **kwargs) -> dict:
        """Create an order"""
        payload = {
            'products': products,
            'billing_address': billing_address,
            **kwargs,
        }
        return self._api.v2.post('/orders', json=payload)

    def update(self, order_id: int, data: dict) -> dict:
        """Update a specific order by its ID"""
        return self._api.v2.put(f'/orders/{order_id}', json=data)

    def archive(self, order_id: int) -> None:
        """Archive a specific order by its ID"""
        self._api.v2.delete(f'/orders/{order_id}')

    def all_products(self, order_id: int) -> Iterator[dict]:
        """Return an iterator for all order products in an order"""
        return self._api.v2.get_many(f'/orders/{order_id}/products')

    def get_product(self, order_id: int, product_id: int) -> dict:
        """Get a specific order product in an order by ID"""
        return self._api.v2.get(f'/orders/{order_id}/products/{product_id}')

    def get_refund_quote(self, order_id: int, *, items: list, **kwargs) -> dict:
        """Get a refund quote for an order by ID"""
        payload = {
            "items": items,
            **kwargs,
        }
        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refund_quotes', json=payload)

    def create_refund(self, order_id: int, *, items: list, payments: list[dict], **kwargs) -> dict:
        """Create a refund for an order by ID"""
        payload = {
            "items": items,
            "payments": payments,
            **kwargs,
        }
        return self._api.v3.post(f'/orders/{order_id}/payment_actions/refunds', json=payload)

    def all_refunds(self, order_id: Optional[int]) -> Iterator[dict]:
        """Return an iterator for all refunds, optionally filtered by order"""
        if order_id:
            endpoint = f'/orders/{order_id}/payment_actions/refunds'
        else:
            endpoint = '/orders/payment_actions/refunds'
        return self._api.v3.get_many(endpoint)

    def get_refund(self, refund_id: int) -> dict:
        """Get a specific refund by its ID"""
        try:
            return self._api.v3.get(f'/orders/payment_actions/refunds?id:in={refund_id}')[0]
        except IndexError:
            raise ResourceNotFoundError()

    def all_shipping_addresses(self, order_id: int) -> Iterator[dict]:
        """Return an iterator for all order shipping addresses in an order"""
        return self._api.v2.get_many(f'/orders/{order_id}/shipping_addresses')

    def get_shipping_address(self, order_id: int, address_id: int) -> dict:
        """Get a specific shipping address in an order by ID"""
        return self._api.v2.get(f'/orders/{order_id}/shipping_addresses/{address_id}')

    def update_shipping_address(self, order_id: int, address_id: int, **kwargs) -> dict:
        """Update a specific shipping address in an order by ID"""
        return self._api.v2.put(f'/orders/{order_id}/shipping_addresses/{address_id}', json=kwargs)

    def all_shipments(self, order_id: int) -> Iterator[dict]:
        """Returns all shipments for a specified order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipments')

    def create_shipment(self, order_id: int, *, order_address_id: int, items: list[dict], **kwargs) -> dict:
        """Creates an order shipment for the specified order"""

        payload = {
            'order_address_id': order_address_id,
            'items': items,
            **kwargs,
        }

        return self._api.v2.post(f'/orders/{order_id}/shipments', json=payload)
