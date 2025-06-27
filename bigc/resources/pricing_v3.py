from typing import Any, Iterator

from bigc.api_client import BigCommerceV3APIClient


class BigCommercePricingV3API:
    def __init__(self, api: BigCommerceV3APIClient):
        self._api = api

    def get_pricing(
            self,
            data: dict[str, Any],
            *,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for batch product pricing"""
        return self._api.post('/pricing/products', data=data, timeout=timeout, retries=retries)
