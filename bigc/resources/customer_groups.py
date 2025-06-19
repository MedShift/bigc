from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCustomerGroupsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all customer groups"""

        return self._api.v2.get_many('/customer_groups', params=params, timeout=timeout)

    def get(self, customer_group_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> dict[str, Any]:
        """Get a specific customer group by its ID"""

        return self._api.v2.get(f'/customer_groups/{customer_group_id}', params=params, timeout=timeout)

    def create(self, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Create a customer group"""

        return self._api.v2.post('/customer_groups', data=data, timeout=timeout)

    def update(self, customer_group_id: int, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Update a specific customer group by its ID"""

        return self._api.v2.put(f'/customer_groups/{customer_group_id}', data=data, timeout=timeout)

    def delete(self, customer_group_id: int, *, timeout: float | None = None) -> dict[str, Any]:
        """Delete a specific customer group by its ID"""

        return self._api.v2.delete(f'/customer_groups/{customer_group_id}', timeout=timeout)
