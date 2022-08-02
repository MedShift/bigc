from collections.abc import Iterator

from bigc._client import BigCommerceV3APIClient


class BigCommercePricingAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def products(self, customer_group_id: int, items: list[dict], channel_id: int = 1,
                 currency_code: str = 'USD') -> Iterator[dict]:
        """Return an iterator for batch product pricing"""
        return self._v3_client.paginated_request('POST', '/pricing/products', json={
            'customer_group_id': customer_group_id,
            'items': items,
            'channel_id': channel_id,
            'currency_code': currency_code,
        })
