from collections.abc import Iterator
from typing import Any, Iterable
from urllib.parse import urlencode, urlparse, urlunparse

from bigc.api_client import BigCommerceAPIClient
from bigc.exceptions import ResourceNotFoundError


class BigCommerceCustomersAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, id_in: Iterable[int] = None, include_formfields: bool = False,
            include_storecredit: bool = False) -> Iterator[dict]:
        """Return an iterator for all customers"""
        url_parts = urlparse('/customers')

        query_dict = {}

        if id_in is not None:
            query_dict['id:in'] = ','.join(map(str, id_in))

        include = []
        if include_storecredit:
            include.append('storecredit')
        if include_formfields:
            include.append('formfields')
        if include:
            query_dict['include'] = ','.join(include)

        url_parts = url_parts._replace(query=urlencode(query_dict))

        return self._api.v3.get_many(urlunparse(url_parts))

    def get(self, customer_id: int, *, include_formfields: bool = False,
            include_storecredit: bool = False) -> dict:
        """Get a specific customer by its ID"""
        url_parts = urlparse('/customers')

        query_dict = {'id:in': customer_id}

        include = []
        if include_storecredit:
            include.append('storecredit')
        if include_formfields:
            include.append('formfields')
        if include:
            query_dict['include'] = ','.join(include)

        url_parts = url_parts._replace(query=urlencode(query_dict))

        try:
            return self._api.v3.get(urlunparse(url_parts))[0]
        except IndexError:
            raise ResourceNotFoundError()

    def create(self, first_name: str, last_name: str, email: str, **kwargs) -> dict:
        """Create a single customer"""
        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            **kwargs,
        }
        return self._api.v3.post('/customers', json=[payload])[0]

    def update(self, customer_id: int, data: dict) -> dict:
        """Update a single customer"""
        payload = {
            'id': customer_id,
            **data,
        }
        return self._api.v3.put('/customers', json=[payload])[0]

    def delete(self, customer_id: int) -> None:
        """Delete a specific customer by its ID"""
        self._api.v3.delete(f'/customers?id:in={customer_id}')

    def update_form_field(self, customer_id: int, field_name: str, value: Any) -> dict:
        """Update a form field value for a single customer"""
        payload = [{
            'customer_id': customer_id,
            'name': field_name,
            'value': value,
        }]
        return self._api.v3.put('/customers/form-field-values', json=payload)[0]

    def all_addresses(self, customer_id: int) -> Iterator[dict]:
        """Get all addresses from a customer's address book"""
        return self._api.v3.get_many(f'/customers/addresses?customer_id:in={customer_id}')

    def get_address(self, customer_id: int, address_id: int) -> dict:
        """Get one address by its ID, from a customer's address book"""
        try:
            return self._api.v3.get(f'/customers/addresses?customer_id:in={customer_id}&id:in={address_id}')[0]
        except IndexError:
            raise ResourceNotFoundError()

    def create_address(self, customer_id: int, **kwargs) -> dict:
        """Add an address to the customer's address book"""
        return self._api.v3.post('/customers/addresses', json=[{'customer_id': customer_id, **kwargs}])

    def update_address(self, address_id: int, **kwargs) -> dict:
        """Update an address by its ID"""
        return self._api.v3.put('/customers/addresses', json=[{'address_id': address_id, **kwargs}])

    def delete_address(self, address_id: int) -> dict:
        """Delete an address by its ID"""
        return self._api.v3.delete(f"/customers/addresses?id:in={address_id}")
