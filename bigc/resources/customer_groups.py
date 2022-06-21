from collections.abc import Iterator

from bigc._client import BigCommerceV2APIClient


class BigCommerceCustomerGroupsAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v2_client = BigCommerceV2APIClient(store_hash, access_token)

    def all(self) -> Iterator[dict]:
        """Return an iterator for all customer groups"""
        return self._v2_client.paginated_request('GET', '/customer_groups')

    def get(self, customer_group_id: int) -> dict:
        """Get a specific customer group by its ID"""
        return self._v2_client.request('GET', f'/customer_groups/{customer_group_id}')

    def create(self, *, name: str, **kwargs) -> dict:
        """Create a customer group"""
        payload = {
            'name': name,
            **kwargs
        }
        return self._v2_client.request('POST', '/customer_groups', json=payload)

    def update(self, customer_group_id: int, data: dict) -> dict:
        """Update a specific customer group by its ID"""
        return self._v2_client.request('PUT', f'/customer_groups/{customer_group_id}', json=data)

    def delete(self, customer_group_id: int) -> dict:
        """Delete a specific customer group by its ID"""
        return self._v2_client.request('DELETE', f'/customer_groups/{customer_group_id}')
