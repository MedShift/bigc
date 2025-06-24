"""
Resources are organized by their URLs and API version. For example, all v3 endpoints that start
with `/customers` reside within `customers_v3.py`.
"""

from .carts_v3 import BigCommerceCartsV3API
from .catalog_v3 import BigCommerceCatalogV3API
from .checkouts_v3 import BigCommerceCheckoutsV3API
from .currencies_v2 import BigCommerceCurrenciesV2API
from .customer_groups_v2 import BigCommerceCustomerGroupsV2API
from .customers_v3 import BigCommerceCustomersV3API
from .orders_v2 import BigCommerceOrdersV2API
from .pricing_v3 import BigCommercePricingV3API
from .webhooks_v3 import BigCommerceWebhooksV3API
from .orders_v3 import BigCommerceOrdersV3API
