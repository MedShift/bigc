from typing import Iterable, Union
from uuid import UUID

from bigc.api_client import BigCommerceAPIClient

UUIDLike = Union[UUID, str]


class BigCommerceCheckoutsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def get(self, checkout_id: UUIDLike, *, include: Iterable[str] = ()) -> dict:
        """Get a specific checkout by its ID"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        return self._api.v3.get(f'/checkouts/{checkout_id}', params=params)

    def update_customer_message(self,
                                checkout_id: UUIDLike,
                                *,
                                customer_message: str,
                                include: Iterable[str] = ()) -> dict:
        """Change customer message pertaining to an existing Checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {'customer_message': customer_message}

        return self._api.v3.put(f'/checkouts/{checkout_id}', params=params, json=payload)

    def add_billing_address(self,
                            checkout_id: UUIDLike,
                            *,
                            email: str,
                            country_code: str,
                            include: Iterable[str] = (),
                            **kwargs) -> dict:
        """Add a billing address to an existing checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {
            'email': email,
            'country_code': country_code,
            **kwargs
        }

        return self._api.v3.post(f'/checkouts/{checkout_id}/billing-address', params=params, json=payload)

    def update_billing_address(self,
                               checkout_id: UUIDLike,
                               address_id: str,
                               *,
                               email: str,
                               country_code: str,
                               include: Iterable[str] = (),
                               **kwargs) -> dict:
        """Update an existing billing address on a checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {
            'email': email,
            'country_code': country_code,
            **kwargs
        }

        return self._api.v3.put(f'/checkouts/{checkout_id}/billing-address/{address_id}', params=params, json=payload)

    def add_consignment(self,
                        checkout_id: UUIDLike,
                        include_available_shipping_options: bool = False,  # deprecated
                        *,
                        include: Iterable[str] = (),
                        **kwargs) -> dict:
        """Add a new consignment to a checkout"""

        # Compatibility code for include_available_shipping_options (deprecated)
        if include_available_shipping_options:
            include = [*include, 'consignments.available_shipping_options']

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = [{**kwargs}]

        return self._api.v3.post(f'/checkouts/{checkout_id}/consignments', params=params, json=payload)

    def update_consignment(self,
                           checkout_id: UUIDLike,
                           consignment_id: str,
                           include_available_shipping_options: bool = False,  # deprecated
                           *,
                           include: Iterable[str] = (),
                           **kwargs) -> dict:
        """Update an existing consignment's selected shipping option"""

        # Compatibility code for include_available_shipping_options (deprecated)
        if include_available_shipping_options:
            include = [*include, 'consignments.available_shipping_options']

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {**kwargs}

        return self._api.v3.put(f'/checkouts/{checkout_id}/consignments/{consignment_id}', params=params, json=payload)

    def delete_consignment(self, checkout_id: UUIDLike, consignment_id: str, *, include: Iterable[str] = ()) -> dict:
        """Remove an existing consignment from a checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        return self._api.v3.delete(f'/checkouts/{checkout_id}/consignments/{consignment_id}', params=params)

    def add_coupon(self, checkout_id: UUIDLike, coupon_code: str, *, include: Iterable[str] = ()) -> dict:
        """Add a coupon code to a checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {'coupon_code': coupon_code}

        return self._api.v3.post(f'/checkouts/{checkout_id}/coupons', params=params, json=payload)

    def delete_coupon(self, checkout_id: UUIDLike, coupon_code: str, *, include: Iterable[str] = ()) -> dict:
        """Delete a coupon code from a checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        return self._api.v3.delete(f'/checkouts/{checkout_id}/coupons/{coupon_code}', params=params)

    def add_discounts(self, checkout_id: UUIDLike, discounts: list, *, include: Iterable[str] = ()) -> dict:
        """Add discounts to an existing checkout"""

        params = {}
        if include:
            params['include'] = ','.join(include)

        payload = {'cart': {'discounts': discounts}}

        return self._api.v3.post(f'/checkouts/{checkout_id}/discounts', params=params, json=payload)

    def create_order(self, checkout_id: UUIDLike) -> dict:
        """Create an order"""
        return self._api.v3.post(f'/checkouts/{checkout_id}/orders')
