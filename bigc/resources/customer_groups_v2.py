from typing import Any, Iterator

from bigc.api_client import BigCommerceV2APIClient


class BigCommerceCustomerGroupsV2API:
    def __init__(self, api: BigCommerceV2APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all customer groups"""
        return self._api.get_many('/customer_groups', params=params, timeout=timeout, retries=retries)

    def get(
            self,
            customer_group_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific customer group by its ID"""
        return self._api.get(f'/customer_groups/{customer_group_id}', params=params, timeout=timeout, retries=retries)

    def create(self, data: dict[str, Any], *, timeout: float | None = None) -> dict[str, Any]:
        """Create a customer group"""
        return self._api.post('/customer_groups', data=data, timeout=timeout)

    def update(
            self,
            customer_group_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Update a specific customer group by its ID"""
        return self._api.put(f'/customer_groups/{customer_group_id}', data=data, timeout=timeout, retries=retries)

    def delete(
            self,
            customer_group_id: int,
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Delete a specific customer group by its ID"""
        return self._api.delete(f'/customer_groups/{customer_group_id}', timeout=timeout, retries=retries)
