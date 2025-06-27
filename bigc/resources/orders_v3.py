from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient
from bigc.exceptions import DoesNotExistError


class BigCommerceOrdersV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def get_refund_quote(
            self,
            order_id: int,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a refund quote for an order by ID"""
        return self._api.post(f'/orders/{order_id}/payment_actions/refund_quotes', data=data, timeout=timeout, retries=retries)

    def create_refund(
            self,
            order_id: int,
            data: dict[str, Any],
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
    ) -> dict[str, Any]:
        """Create a refund for an order by ID"""
        return self._api.post(f'/orders/{order_id}/payment_actions/refunds', data=data, params=params, timeout=timeout)

    def all_refunds(
            self,
            order_id: int | None = None,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all refunds, optionally filtered by order"""
        if order_id:
            endpoint = f'/orders/{order_id}/payment_actions/refunds'
        else:
            endpoint = '/orders/payment_actions/refunds'

        return self._api.get_many(endpoint, params=params, timeout=timeout, retries=retries)

    def get_refund(
            self,
            refund_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> dict[str, Any]:
        """Get a specific refund by its ID"""
        params = {
            **(params or {}),
            'id:in': refund_id,
        }

        try:
            return self._api.get('/orders/payment_actions/refunds', params=params, timeout=timeout, retries=retries)[0]
        except IndexError:
            raise DoesNotExistError() from None
