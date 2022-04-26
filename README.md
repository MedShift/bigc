# bigc

An unofficial Python client for the BigCommerce API.

_This project is currently in an alpha state._

## Installation

```shell
pip install bigc 
```

## Usage

To authenticate, you'll need the BigCommerce store's hash and an access token.

```python
from bigc import BigCommerceAPI


store_hash = '000000000'
access_token = '0000000000000000000000000000000'
bigcommerce = BigCommerceAPI(store_hash, access_token)

order: dict = bigcommerce.orders.get(101)
orders: list[dict] = list(bigcommerce.orders.all(customer_id=1))
```

The following resources are currently supported:

- `carts`
- `customers`
- `orders`
- `products`
- `product_variants`
- `webhooks`

### Utilities

Some extra utility functions that don't interact with the BigCommerce API are available in `bigc.utils`.

- `bigc.utils.parse_rfc2822_date`: Convert an RFC-2822 date (used by some BigCommerce APIs) to a `datetime`

### Constants

For convenience, some constants are made available in `bigc.data`.

- `bigc.data.BigCommerceOrderStatus`: An `Enum` of order statuses and their IDs
