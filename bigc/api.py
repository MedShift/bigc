from bigc.api_client import BigCommerceV2APIClient, BigCommerceV3APIClient
from bigc.resources import *


class BigCommerceAPI:
    def __init__(
            self,
            store_hash: str,
            access_token: str,
            *,
            timeout: float | None = None,
            get_retries: int | None = None
    ):
        api_v2 = BigCommerceV2APIClient(store_hash, access_token, timeout=timeout, get_retries=get_retries)
        api_v3 = BigCommerceV3APIClient(store_hash, access_token, timeout=timeout, get_retries=get_retries)

        self.api_v2 = api_v2
        self.api_v3 = api_v3

        self.carts_v3: BigCommerceCartsV3API = BigCommerceCartsV3API(api_v3)
        self.categories_v3: BigCommerceCategoriesV3API = BigCommerceCategoriesV3API(api_v3)
        self.checkouts_v3: BigCommerceCheckoutsV3API = BigCommerceCheckoutsV3API(api_v3)
        self.currencies_v2: BigCommerceCurrenciesV2API = BigCommerceCurrenciesV2API(api_v2)
        self.customer_groups_v2: BigCommerceCustomerGroupsV2API = BigCommerceCustomerGroupsV2API(api_v2)
        self.customers_v3: BigCommerceCustomersV3API = BigCommerceCustomersV3API(api_v3)
        self.orders_v2: BigCommerceOrdersV2API = BigCommerceOrdersV2API(api_v2)
        self.orders_v3: BigCommerceOrdersV3API = BigCommerceOrdersV3API(api_v3)
        self.pricing_v3: BigCommercePricingV3API = BigCommercePricingV3API(api_v3)
        self.product_variants_v3: BigCommerceProductVariantsV3API = BigCommerceProductVariantsV3API(api_v3)
        self.products_v3: BigCommerceProductsV3API = BigCommerceProductsV3API(api_v3)
        self.webhooks_v3: BigCommerceWebhooksV3API = BigCommerceWebhooksV3API(api_v3)
