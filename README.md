# bigc
*An unofficial Python client for the BigCommerce API*

## Installation

```shell
pip install bigc
```

## Usage

To authenticate, you'll need the BigCommerce store's hash and an access token.

```python
from bigc import BigCommerceAPI
from typing import Any

store_hash = '000000000'
access_token = '0000000000000000000000000000000'
bigcommerce = BigCommerceAPI(store_hash, access_token)

order: dict[str, Any] = bigcommerce.orders_v2.get(101)
orders: list[dict[str, Any]] = list(bigcommerce.orders_v2.all(params={'customer_id': 1}))
```

The following resources are currently supported:

- `carts_v3`
- `checkouts_v3`
- `currencies_v2`
- `customer_groups_v2`
- `customers_v3`
- `orders_v2`
- `orders_v3`
- `pricing_v3`
- `product_categories_v3`
- `product_variants_v3`
- `products_v3`
- `webhooks_v3`


### Direct API Access
For resources or parameters that aren't officially supported yet, bigc also includes a flexible API client that can be used to make direct requests to the BigCommerce API.

```python
bigcommerce = BigCommerceAPI(store_hash, access_token)

product = bigcommerce.api_v3.get('/products/77', params={'include': 'videos'})
order_messages = bigcommerce.api_v2.get_many('/orders/101/messages')  # get_many provides automatic pagination
```

### Additional Functionality
- Built-in retry handling:
  - `GET` requests are automatically retried for some server & network errors.
- HTTP errors are transformed into exceptions, see `bigc/exceptions.py`.
  - Error responses are parsed to provide `e.message` and `e.errors`.

### Utilities

Some extra utility functions that don't interact with the BigCommerce API are available in `bigc.utils`.

- `bigc.utils.parse_rfc2822_date`: Convert an [RFC-2822 date] (used by some BigCommerce APIs) to a `datetime`

[RFC-2822 date]: https://www.rfc-editor.org/rfc/rfc2822#section-3.3

### Constants

For convenience, some constants are made available in `bigc.data`.

- `bigc.data.BigCommerceOrderStatus`: An `Enum` of order statuses and their IDs
