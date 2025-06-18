from typing import Any, Iterator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceCustomerGroupsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Iterator[dict[str, Any]]:
        """Return an iterator for all customer groups"""

        return self._api.v2.get_many('/customer_groups', **kwargs)

    def get(self, customer_group_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific customer group by its ID"""

        return self._api.v2.get(f'/customer_groups/{customer_group_id}', **kwargs)

    def create(self, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a customer group"""

        return self._api.v2.post('/customer_groups', json=data, **kwargs)

    def update(self, customer_group_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific customer group by its ID"""

        return self._api.v2.put(f'/customer_groups/{customer_group_id}', json=data, **kwargs)

    def delete(self, customer_group_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Delete a specific customer group by its ID"""

        return self._api.v2.delete(f'/customer_groups/{customer_group_id}', **kwargs)
