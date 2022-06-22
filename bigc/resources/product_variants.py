from collections.abc import Iterator

from bigc._client import BigCommerceV3APIClient


class BigCommerceProductVariantsAPI:
    def __init__(self, store_hash: str, access_token: str):
        self._v3_client = BigCommerceV3APIClient(store_hash, access_token)

    def all(self, product_id: int) -> Iterator[dict]:
        """Return an iterator for all variants of a product"""
        return self._v3_client.paginated_request('GET', f'/catalog/products/{product_id}/variants')

    def get(self, product_id: int, variant_id: int) -> dict:
        """Get a specific product variant by ID"""
        return self._v3_client.request('GET', f'/catalog/products/{product_id}/variants/{variant_id}')

    def create(self, product_id: int, *, sku: str, option_values: list[dict], **kwargs) -> dict:
        """Create a product variant"""
        payload = {
            'sku': sku,
            'option_values': option_values,
            **kwargs,
        }
        return self._v3_client.request('POST', f'/catalog/products/{product_id}/variants', json=payload)

    def update(self, product_id: int, variant_id: int, data: dict) -> dict:
        """Update a specific product variant by its ID"""
        return self._v3_client.request('PUT', f'/catalog/products/{product_id}/variants/{variant_id}', json=data)

    def delete(self, product_id: int, variant_id: int) -> dict:
        """Delete a specific product variant by its ID"""
        return self._v3_client.request('DELETE', f'/catalog/products/{product_id}/variants/{variant_id}')
