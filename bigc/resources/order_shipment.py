from typing import Iterator, Optional

from bigc.api_client import BigCommerceAPIClient
from bigc.data import BigCommerceShippingMethod, BigCommerceShippingProvider


class BigCommerceOrderShipmentsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, order_id: int) -> Iterator[dict]:
        """Returns all shipments for a specified order"""

        return self._api.v2.get_many(f'/orders/{order_id}/shipments')

    def create(
            self,
            order_id: int,
            order_address_id: int,
            items: list[dict],
            *,
            tracking_number: Optional[str] = None,
            shipping_method: Optional[BigCommerceShippingMethod] = None,
            shipping_provider: Optional[BigCommerceShippingProvider] = None,
            tracking_carrier: Optional[str] = None,
            comments: Optional[str] = None,
            **kwargs,
    ) -> dict:
        """Creates an order shipment for the specified order"""

        optional_params = {k: v for k, v in {
            'tracking_number': tracking_number,
            'shipping_method': shipping_method,
            'shipping_provider': shipping_provider,
            'tracking_carrier': tracking_carrier,
            'comments': comments
        }.items() if v is not None}

        payload = {
            'order_address_id': order_address_id,
            'items': items,
            **optional_params,
            **kwargs,
        }

        return self._api.v2.post(f'/orders/{order_id}/shipments', json=payload)
