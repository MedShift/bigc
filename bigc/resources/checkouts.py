from typing import Any, TypeAlias
from uuid import UUID

from bigc.api_client import BigCommerceAPIClient

UUIDLike: TypeAlias = UUID | str


class BigCommerceCheckoutsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def get(self, checkout_id: UUIDLike, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific checkout by its ID"""

        return self._api.v3.get(f'/checkouts/{checkout_id}', params=params, timeout=timeout)

    def update(self, checkout_id: UUIDLike, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Change customer message pertaining to an existing Checkout"""

        return self._api.v3.put(f'/checkouts/{checkout_id}', json=data, timeout=timeout)

    def add_billing_address(self, checkout_id: UUIDLike, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Add a billing address to an existing checkout"""

        return self._api.v3.post(f'/checkouts/{checkout_id}/billing-address', json=data, timeout=timeout)

    def update_billing_address(
        self,
        checkout_id: UUIDLike,
        address_id: str,
        data: dict[str, Any],
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Update an existing billing address on a checkout"""

        return self._api.v3.put(f'/checkouts/{checkout_id}/billing-address/{address_id}', json=data, timeout=timeout)

    def add_consignment(
        self,
        checkout_id: UUIDLike,
        data: dict[str, Any],
        params: dict[str, Any] | None = None, timeout: float | None = None,
    ) -> dict[str, Any]:
        """Add a new consignment to a checkout"""

        return self._api.v3.post(f'/checkouts/{checkout_id}/consignments', json=data, params=params, timeout=timeout)

    def update_consignment(
        self,
        checkout_id: UUIDLike,
        consignment_id: str,
        data: dict[str, Any],
        params: dict[str, Any] | None = None, timeout: float | None = None,
    ) -> dict[str, Any]:
        """Update an existing consignment's selected shipping option"""

        return self._api.v3.put(f'/checkouts/{checkout_id}/consignments/{consignment_id}', json=data, params=params, timeout=timeout)

    def delete_consignment(self, checkout_id: UUIDLike, consignment_id: str, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Remove an existing consignment from a checkout"""

        return self._api.v3.delete(f'/checkouts/{checkout_id}/consignments/{consignment_id}', params=params, timeout=timeout)

    def add_coupon(self, checkout_id: UUIDLike, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Add a coupon code to a checkout"""

        return self._api.v3.post(f'/checkouts/{checkout_id}/coupons', json=data, params=params, timeout=timeout)

    def delete_coupon(self, checkout_id: UUIDLike, coupon_code: str, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Delete a coupon code from a checkout"""

        return self._api.v3.delete(f'/checkouts/{checkout_id}/coupons/{coupon_code}', params=params, timeout=timeout)

    def add_discounts(self, checkout_id: UUIDLike, data: dict[str, Any], *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Add discounts to an existing checkout"""

        return self._api.v3.post(f'/checkouts/{checkout_id}/discounts', json=data, params=params, timeout=timeout)

    def create_order(self, checkout_id: UUIDLike, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Create an order"""

        return self._api.v3.post(f'/checkouts/{checkout_id}/orders', params=params, timeout=timeout)
