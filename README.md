# bigc

An unofficial Python client for the BigCommerce API.

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

order = bigcommerce.orders_v2.get(101)
list_of_orders = list(bigcommerce.orders_v2.all(params={'customer_id': 1}))
```

The following resources are currently supported:

- `carts_v3`
- `categories_v3`
- `checkouts_v3`
- `currencies_v2`
- `customers_v3`
- `customer_groups_v2`
- `orders_v2`
- `orders_v3`
- `pricing_v3`
- `products_v3`
- `product_variants_v3`
- `webhooks_v3`

### Exceptions

If a request is not successful, `bigc` will raise an exception inheriting from `BigCommerceException`. The full exception hierarchy is available in `bigc.exceptions`. Most exceptions correspond to a specific status code (e.g. `DoesNotExistError` will be raised for 404s).

If BigCommerce provides an error message in its response, it will be available as `exc.message`. More detailed error information may be available as `exc.errors`.

### Timeouts

A timeout may be set on individual requests, or a default may be set for all requests. This specifies the maximum amount of time, in seconds, that may pass between receiving data from the server.

If a request times out, a `GatewayTimeoutError` will be raised.

```python
from bigc import BigCommerceAPI

bigcommerce = BigCommerceAPI('store_hash', 'access_token', timeout=7)
bigcommerce.checkouts_v3.create_order('checkout_id', timeout=16)
```

### Automatic Retries

`bigc` can automatically retry requests that fail due to network problems or certain types of server errors. You can specify the maximum number of retries as a default for all `GET` requests, or on a per-request basis.

```python
from bigc import BigCommerceAPI

bigcommerce = BigCommerceAPI('store_hash', 'access_token', get_retries=2)
bigcommerce.customers_v3.get(1, retries=5)
```

### Connection Pooling

Requests are made through a [`requests.Session`], so connections are pooled and reused instead of reopened for each request. This needs no setup, and applies across both the v2 and v3 APIs, which share one session.

The pool belongs to the `BigCommerceAPI` instance, so reuse a single instance rather than creating one per request. A `requests.Session` is not thread-safe, so each thread should use its own instance.

The session is exposed as `bigcommerce.session` if you need to configure it, e.g. to `mount()` an adapter with a larger `pool_maxsize`. To reuse a session your application has already configured, pass it as `session`.

[`requests.Session`]: https://requests.readthedocs.io/en/latest/user/advanced/#session-objects

### Direct API Access

For resources that aren't officially supported yet, `bigc` also includes a flexible API client that can be used to make direct requests to the BigCommerce API.

```python
from bigc import BigCommerceAPI

bigcommerce = BigCommerceAPI('store_hash', 'access_token')

product = bigcommerce.api_v3.get('/products/77', params={'include': 'videos'})
order_messages = list(bigcommerce.api_v2.get_many('/orders/101/messages'))
```

### Utilities

Some extra utility functions that don't interact with the BigCommerce API are available in `bigc.utils`.

- `bigc.utils.parse_rfc2822_date`: Convert an [RFC-2822 date] (used by some BigCommerce APIs) to a `datetime`

[RFC-2822 date]: https://www.rfc-editor.org/rfc/rfc2822#section-3.3

### Constants

For convenience, some constants are made available in `bigc.data`.

- `bigc.data.BigCommerceOrderStatus`: An `IntEnum` of order statuses and their IDs

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and packaging.

### Setup

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv sync` to install dependencies and set up a virtual environment

### Running Tests

```shell
uv run pytest
```
