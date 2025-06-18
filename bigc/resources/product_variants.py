from typing import Any, Iterator, Unpack

from bigc.api_client import BigCommerceAPIClient, RequestOptions


class BigCommerceProductVariantsAPI:
    def __init__(self, api_client: BigCommerceAPIClient):
        self._api = api_client

    def all(self, product_id: int, **kwargs: Unpack[RequestOptions]) -> Iterator[dict[str, Any]]:
        """Return an iterator for all variants of a product"""

        return self._api.v3.get_many(f'/catalog/products/{product_id}/variants', **kwargs)

    def get(self, product_id: int, variant_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Get a specific product variant by ID"""

        return self._api.v3.get(f'/catalog/products/{product_id}/variants/{variant_id}', **kwargs)

    def create(self, product_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Create a product variant"""

        return self._api.v3.post(f'/catalog/products/{product_id}/variants', json=data, **kwargs)

    def update(self, product_id: int, variant_id: int, data: dict[str, Any], **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Update a specific product variant by its ID"""

        return self._api.v3.put(f'/catalog/products/{product_id}/variants/{variant_id}', json=data, **kwargs)

    def delete(self, product_id: int, variant_id: int, **kwargs: Unpack[RequestOptions]) -> dict[str, Any]:
        """Delete a specific product variant by its ID"""

        return self._api.v3.delete(f'/catalog/products/{product_id}/variants/{variant_id}', **kwargs)
