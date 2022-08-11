from collections.abc import Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCustomerGroupsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self) -> Iterator[dict]:
        """Return an iterator for all customer groups"""
        return self._api.v2.get_many('/customer_groups')

    def get(self, customer_group_id: int) -> dict:
        """Get a specific customer group by its ID"""
        return self._api.v2.get(f'/customer_groups/{customer_group_id}')

    def create(self, *, name: str, **kwargs) -> dict:
        """Create a customer group"""
        payload = {
            'name': name,
            **kwargs
        }
        return self._api.v2.post('/customer_groups', json=payload)

    def update(self, customer_group_id: int, data: dict) -> dict:
        """Update a specific customer group by its ID"""
        return self._api.v2.put(f'/customer_groups/{customer_group_id}', json=data)

    def delete(self, customer_group_id: int) -> dict:
        """Delete a specific customer group by its ID"""
        return self._api.v2.delete(f'/customer_groups/{customer_group_id}')
