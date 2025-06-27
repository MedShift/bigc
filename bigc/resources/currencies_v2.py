from typing import Any, Iterator

from bigc.api_client import BigCommerceV2APIClient


class BigCommerceCurrenciesV2API:
    def __init__(self, api: BigCommerceV2APIClient):
        self._api = api

    def all(
            self,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Return an iterator for all currencies"""
        return self._api.get_many('/currencies', params=params, timeout=timeout, retries=retries)

    def get(
            self,
            currency_id: int,
            *,
            params: dict[str, Any] | None = None,
            timeout: float | None = None,
            retries: int | None = None,
    ):
        """Get a specific currency by its ID"""
        return self._api.get(f'/currencies/{currency_id}', params=params, timeout=timeout, retries=retries)
