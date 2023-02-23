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
- `categories`
- `checkouts`
- `customer_groups`
- `customers`
- `orders`
- `products`
- `product_variants`
- `webhooks`

### Direct API Access

For resources or parameters that aren't officially supported yet, bigc also includes a flexible API client that can be used to make direct requests to the BigCommerce API.

```python
bigcommerce = BigCommerceAPI(store_hash, access_token)

product = bigcommerce.api.v3.get('/products/77', params={'include': 'videos'})
order_messages = bigcommerce.api.v2.get_many('/orders/101/messages')
```

### Utilities

Some extra utility functions that don't interact with the BigCommerce API are available in `bigc.utils`.

- `bigc.utils.parse_rfc2822_date`: Convert an [RFC-2822 date] (used by some BigCommerce APIs) to a `datetime`

[RFC-2822 date]: https://www.rfc-editor.org/rfc/rfc2822#section-3.3

### Constants

For convenience, some constants are made available in `bigc.data`.

- `bigc.data.BigCommerceOrderStatus`: An `Enum` of order statuses and their IDs
