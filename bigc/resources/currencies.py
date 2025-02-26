from collections.abc import Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceCurrenciesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self.api = api_client

    def all(self) -> Iterator[dict]:
        """Return an iterator for all currencies"""
        return self.api.v2.get_many('/currencies')

    def get(self, currency_id: int):
        """Get a specific currency by its ID"""
        return self.api.v2.get(f'/currencies/{currency_id}')
