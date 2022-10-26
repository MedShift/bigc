from collections.abc import Iterator

from bigc.api_client import BigCommerceAPIClient


class BigCommerceProductVariantsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, product_id: int) -> Iterator[dict]:
        """Return an iterator for all variants of a product"""
        return self._api.v3.get_many(f'/catalog/products/{product_id}/variants')

    def get(self, product_id: int, variant_id: int) -> dict:
        """Get a specific product variant by ID"""
        return self._api.v3.get(f'/catalog/products/{product_id}/variants/{variant_id}')

    def create(self, product_id: int, *, sku: str, option_values: list[dict], **kwargs) -> dict:
        """Create a product variant"""
        payload = {
            'sku': sku,
            'option_values': option_values,
            **kwargs,
        }
        return self._api.v3.post(f'/catalog/products/{product_id}/variants', json=payload)

    def update(self, product_id: int, variant_id: int, data: dict) -> dict:
        """Update a specific product variant by its ID"""
        return self._api.v3.put(f'/catalog/products/{product_id}/variants/{variant_id}', json=data)

    def delete(self, product_id: int, variant_id: int) -> dict:
        """Delete a specific product variant by its ID"""
        return self._api.v3.delete(f'/catalog/products/{product_id}/variants/{variant_id}')
