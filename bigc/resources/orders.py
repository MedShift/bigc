from collections.abc import Iterator
from typing import Optional
from urllib.parse import urlparse, urlunparse, urlencode

from bigc.exceptions import ResourceNotFoundError
from bigc._client import BigCommerceV2APIClient, BigCommerceV3APIClient


class BigCommerceOrdersAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v2_client = BigCommerceV2APIClient(store_hash, access_token)
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self, *, customer_id: Optional[int] = None) -> Iterator[dict]:
        """Return an iterator for all orders"""
        url_parts = urlparse('/orders')

        query_dict = {}
        if customer_id:
            query_dict['customer_id'] = str(customer_id)
        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._v2_client.paginated_request('GET', urlunparse(url_parts))

    def get(self, order_id: int) -> dict:
        """Get an order by its ID"""
        return self._v2_client.request('GET', f'/orders/{order_id}')

    def all_products(self, order_id: int) -> Iterator[dict]:
        """Return an iterator for all order products in an order"""
        return self._v2_client.paginated_request('GET', f'/orders/{order_id}/products')

    def get_product(self, order_id: int, product_id: int) -> dict:
        """Get a specific order product in an order by ID"""
        return self._v2_client.request('GET', f'/orders/{order_id}/products/{product_id}')

    def all_refunds(self, order_id: Optional[int]) -> Iterator[dict]:
        """Return an iterator for all refunds, optionally filtered by order"""
        if order_id:
            endpoint = f'/orders/{order_id}/payment_actions/refunds'
        else:
            endpoint = '/orders/payment_actions/refunds'
        return self._v3_client.paginated_request('GET', endpoint)

    def get_refund(self, refund_id: int) -> dict:
        """Get a specific refund by its ID"""
        try:
            return self._v3_client.request('GET', f'/orders/payment_actions/refunds?id:in={refund_id}')[0]
        except IndexError:
            raise ResourceNotFoundError()

    def all_shipping_addresses(self, order_id: int) -> Iterator[dict]:
        """Return an iterator for all order shipping addresses in an order"""
        return self._v2_client.paginated_request('GET', f'/orders/{order_id}/shipping_addresses')

    def get_shipping_address(self, order_id: int, address_id: int) -> dict:
        """Get a specific shipping address in an order by ID"""
        return self._v2_client.request('GET', f'/orders/{order_id}/shipping_addresses/{address_id}')
