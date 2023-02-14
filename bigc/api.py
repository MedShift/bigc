from bigc.api_client import BigCommerceAPIClient
from bigc.resources import *


class BigCommerceAPI:
    def __init__(self, store_hash: str, access_token: str):
        api_client = BigCommerceAPIClient(store_hash, access_token)

        self.carts: BigCommerceCartsAPI = BigCommerceCartsAPI(api_client)
        self.categories: BigCommerceCategoriesAPI = BigCommerceCategoriesAPI(api_client)
        self.checkouts: BigCommerceCheckoutsAPI = BigCommerceCheckoutsAPI(api_client)
        self.customer_groups: BigCommerceCustomerGroupsAPI = BigCommerceCustomerGroupsAPI(api_client)
        self.customers: BigCommerceCustomersAPI = BigCommerceCustomersAPI(api_client)
        self.orders: BigCommerceOrdersAPI = BigCommerceOrdersAPI(api_client)
        self.products: BigCommerceProductsAPI = BigCommerceProductsAPI(api_client)
        self.product_variants: BigCommerceProductVariantsAPI = BigCommerceProductVariantsAPI(api_client)
        self.webhooks: BigCommerceWebhooksAPI = BigCommerceWebhooksAPI(api_client)

        self.api: BigCommerceAPIClient = api_client
