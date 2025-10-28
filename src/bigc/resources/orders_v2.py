from typing import Any, Iterator

from bigc.api_client import BigCommerceV2APIClient


class BigCommerceOrdersV2API:
    def __init__(self, api: BigCommerceV2APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all orders"""
        return self._api.get_many('/orders', params=params, timeout=timeout, retries=retries)

    def get(
            self,
            order_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get an order by its ID"""
        return self._api.get(f'/orders/{order_id}', params=params, timeout=timeout, retries=retries)

    def create(
            self,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create an order"""
        return self._api.post('/orders', data=data, params=params, timeout=timeout)

    def update(
            self,
            order_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific order by its ID"""
        return self._api.put(f'/orders/{order_id}', data=data, timeout=timeout, retries=retries)

    def archive(
            self,
            order_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Archive a specific order by its ID"""
        self._api.delete(f'/orders/{order_id}', timeout=timeout, retries=retries)

    def all_products(
            self,
            order_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all order products in an order"""
        return self._api.get_many(f'/orders/{order_id}/products', params=params, timeout=timeout, retries=retries)

    def get_product(
            self,
            order_id: int,
            product_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific order product in an order by ID"""
        return self._api.get(f'/orders/{order_id}/products/{product_id}', timeout=timeout, retries=retries)

    def all_shipping_addresses(
            self,
            order_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all order shipping addresses in an order"""
        return self._api.get_many(f'/orders/{order_id}/shipping_addresses', params=params, timeout=timeout, retries=retries)

    def get_shipping_address(
            self,
            order_id: int,
            address_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific shipping address in an order by ID"""
        return self._api.get(f'/orders/{order_id}/shipping_addresses/{address_id}', timeout=timeout, retries=retries)

    def update_shipping_address(
            self,
            order_id: int,
            address_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific shipping address in an order by ID"""
        return self._api.put(f'/orders/{order_id}/shipping_addresses/{address_id}', data=data, timeout=timeout, retries=retries)

    def all_shipments(
            self,
            order_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Returns all shipments for a specified order"""
        return self._api.get_many(f'/orders/{order_id}/shipments', params=params, timeout=timeout, retries=retries)

    def get_shipment(
            self,
            order_id: int,
            shipment_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a shipment by its ID"""
        return self._api.get(f'/orders/{order_id}/shipments/{shipment_id}', timeout=timeout, retries=retries)

    def create_shipment(self, order_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Creates an order shipment for the specified order"""
        return self._api.post(f'/orders/{order_id}/shipments', data=data, timeout=timeout)

    def update_shipment(
            self,
            order_id: int,
            shipment_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Updates an order shipment for the specified order"""
        return self._api.put(f'/orders/{order_id}/shipments/{shipment_id}', data=data, timeout=timeout, retries=retries)

    def delete_shipment(
            self,
            order_id: int,
            shipment_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Deletes specific shipment by its ID"""
        return self._api.delete(f'/orders/{order_id}/shipments/{shipment_id}', timeout=timeout, retries=retries)

    def all_coupons(
            self,
            order_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all coupons in an order"""
        return self._api.get_many(f'/orders/{order_id}/coupons', params=params, timeout=timeout, retries=retries)
