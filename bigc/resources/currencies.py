from typing import Any, Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCurrenciesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self.api = api_client

    def all(self, *, params: dict[str, Any] | None = None, timeout: float | None = None) -> Iterator[dict[str, Any]]:
        """Return an iterator for all currencies"""

        return self.api.v2.get_many('/currencies', params=params, timeout=timeout)

    def get(self, currency_id: int, *, params: dict[str, Any] | None = None, timeout: float | None = None):
        """Get a specific currency by its ID"""

        return self.api.v2.get(f'/currencies/{currency_id}', params=params, timeout=timeout)
