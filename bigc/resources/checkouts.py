from typing import Union
from urllib.parse import urlencode, urlparse, urlunparse
from uuid import UUID

from bigc.api_client import BigCommerceAPIClient

UUIDLike = Union[UUID, str]


class BigCommerceCheckoutsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def get(self, checkout_id: UUIDLike) -> dict:
        """Get a specific checkout by its ID"""
        return self._api.v3.get(f'/checkouts/{checkout_id}')

    def update_customer_message(self, checkout_id: UUIDLike, *, customer_message: str) -> dict:
        """Change customer message pertaining to an existing Checkout"""
        payload = {'customer_message': customer_message}
        return self._api.v3.put(f'/checkouts/{checkout_id}', json=payload)

    def add_billing_address(self, checkout_id: UUIDLike, *, email: str, country_code: str, **kwargs) -> dict:
        """Add a billing address to an existing checkout"""
        payload = {'email': email, 'country_code': country_code, **kwargs}
        return self._api.v3.post(f'/checkouts/{checkout_id}/billing-address', json=payload)

    def update_billing_address(self, checkout_id: UUIDLike, address_id: str, *, email: str, country_code: str,
                               **kwargs) -> dict:
        """Update an existing billing address on a checkout"""
        payload = {'email': email, 'country_code': country_code, **kwargs}
        return self._api.v3.put(f'/checkouts/{checkout_id}/billing-address/{address_id}', json=payload)

    def add_consignment(self, checkout_id: UUIDLike,
                        include_available_shipping_options: bool = False,
                        **kwargs) -> dict:
        """Add a new consignment to a checkout"""
        url_parts = urlparse(f'/checkouts/{checkout_id}/consignments')

        include = []
        if include_available_shipping_options:
            include.append('consignments.available_shipping_options')

        query_dict = {}
        if include:
            query_dict['include'] = ','.join(include)

        url_parts = url_parts._replace(query=urlencode(query_dict))

        payload = [{**kwargs}]
        return self._api.v3.post(urlunparse(url_parts), json=payload)

    def update_consignment(self, checkout_id: UUIDLike, consignment_id: str,
                           include_available_shipping_options: bool = False,
                           **kwargs) -> dict:
        """Update an existing consignment's selected shipping option"""
        url_parts = urlparse(f'/checkouts/{checkout_id}/consignments/{consignment_id}')

        include = []
        if include_available_shipping_options:
            include.append('consignments.available_shipping_options')

        query_dict = {}
        if include:
            query_dict['include'] = ','.join(include)

        url_parts = url_parts._replace(query=urlencode(query_dict))

        payload = {**kwargs}
        return self._api.v3.put(urlunparse(url_parts), json=payload)

    def delete_consignment(self, checkout_id: UUIDLike, consignment_id: str) -> dict:
        """Remove an existing consignment from a checkout"""
        return self._api.v3.delete(f'/checkouts/{checkout_id}/consignments/{consignment_id}')

    def add_coupon(self, checkout_id: UUIDLike, coupon_code: str) -> dict:
        """Add a coupon code to a checkout"""
        payload = {'coupon_code': coupon_code}
        return self._api.v3.post(f'/checkouts/{checkout_id}/coupons', json=payload)

    def delete_coupon(self, checkout_id: UUIDLike, coupon_code: str) -> dict:
        """Delete a coupon code from a checkout"""
        return self._api.v3.delete(f'/checkouts/{checkout_id}/coupons/{coupon_code}')

    def add_discounts(self, checkout_id: UUIDLike, discounts: list) -> dict:
        """Add discounts to an existing checkout"""
        payload = {'cart': {'discounts': discounts}}
        return self._api.v3.post(f'/checkouts/{checkout_id}/discounts', json=payload)

    def create_order(self, checkout_id: UUIDLike) -> dict:
        """Create an order"""
        return self._api.v3.post(f'/checkouts/{checkout_id}/orders')
