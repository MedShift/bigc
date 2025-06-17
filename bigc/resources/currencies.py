from typing import Any, Generator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceCurrenciesAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self.api = api_client

    def all(self, **kwargs: Unpack[RequestOptions]) -> Generator[dict[str, Any], None,  None]:
        """Return an iterator for all currencies"""

        return self.api.v2.get_many('/currencies', **kwargs)

    def get(self, currency_id: int, **kwargs: Unpack[RequestOptions]):
        """Get a specific currency by its ID"""

        return self.api.v2.get(f'/currencies/{currency_id}', **kwargs)
