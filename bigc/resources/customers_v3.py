from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient
from bigc.exceptions import DoesNotExistError, InvalidDataError


class BigCommerceCustomersV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all customers"""
        return self._api.get_many('/customers', params=params, timeout=timeout, retries=retries, cursor=True)

    def get(
            self,
            customer_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific customer by its ID"""
        params = {
            **(params or {}),
            'id:in': customer_id,
        }

        try:
            return self._api.get('/customers', params=params, timeout=timeout, retries=retries)[0]
        except IndexError:
            raise DoesNotExistError() from None

    def create_many(self, data: list[dict[str, Any]], *, timeout: float | None = None) -> list[dict[str, Any]]:
        """Create many customers"""
        return self._api.post('/customers', data=data, timeout=timeout)

    def create(self, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Create a single customer"""
        return self.create_many([data], timeout=timeout)[0]

    def update_many(
            self,
            data: list[dict[str, Any]],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> list[dict[str, Any]]:
        """Update many customers"""
        return self._api.put('/customers', data=data, timeout=timeout, retries=retries)

    def update(
            self,
            customer_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a single customer"""
        data['id'] = customer_id

        return self.update_many([data], timeout=timeout, retries=retries)[0]

    def delete_many(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Delete many customers"""
        self._api.delete(f'/customers', params=params, timeout=timeout, retries=retries)

    def delete(
            self,
            customer_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Delete a single customer"""
        params = {
            **(params or {}),
            'id:in': customer_id,
        }

        self.delete_many(params=params, timeout=timeout, retries=retries)

    def update_form_fields(
            self,
            data: list[dict[str, Any]],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> list[dict[str, Any]]:
        """Update form-field values"""
        return self._api.put('/customers/form-field-values', data=data, timeout=timeout, retries=retries)

    def update_form_field(
            self,
            customer_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a single form-field value"""
        return self.update_form_fields([{'customer_id': customer_id, **data}], timeout=timeout, retries=retries)[0]

    def all_addresses(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Get all addresses, optionally filtered by a customer's address book"""
        return self._api.get_many(f'/customers/addresses', params=params, timeout=timeout, retries=retries)

    def get_address(
            self,
            customer_id: int,
            address_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get one address by its ID, from a customer's address book"""
        params = {
            **(params or {}),
            'customer_id:in': customer_id,
            'id:in': address_id,
        }

        try:
            return self._api.get(f'/customers/addresses', params=params, timeout=timeout, retries=retries)[0]
        except IndexError:
            raise DoesNotExistError() from None

    def create_addresses(self, data: list[dict[str, Any]], *, timeout: float | None = None) -> list[dict[str, Any]]:
        """Create many addresses"""
        return self._api.post('/customers/addresses', data=data, timeout=timeout)

    def create_address(self, customer_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Add an address to the customer's address book"""
        try:
            return self.create_addresses([{'customer_id': customer_id, **data}], timeout=timeout)[0]
        except IndexError:
            raise InvalidDataError('This address already exists.') from None

    def update_addresses(
            self,
            data: list[dict[str, Any]],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> list[dict[str, Any]]:
        """Update many addresses"""
        return self._api.put('/customers/addresses', data=data, timeout=timeout, retries=retries)

    def update_address(
            self,
            address_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update an address by its ID"""
        try:
            return self.update_addresses([{'id': address_id, **data}], timeout=timeout, retries=retries)[0]
        except IndexError:
            raise InvalidDataError('This address already exists.') from None

    def delete_addresses(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Delete many addresses"""
        self._api.delete(f"/customers/addresses", params=params, timeout=timeout, retries=retries)

    def delete_address(
            self,
            address_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> None:
        """Delete an address by its ID"""
        params = {
            **(params or {}),
            'id:in': address_id,
        }

        self.delete_addresses(params=params, timeout=timeout, retries=retries)
