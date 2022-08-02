from bigc.resources import *


class BigCommerceAPI:
    def __init__(self, store_hash: str, access_token: str):
        self.carts: BigCommerceCartsAPI = BigCommerceCartsAPI(store_hash, access_token)
        self.categories: BigCommerceCategoriesAPI = BigCommerceCategoriesAPI(store_hash, access_token)
        self.customer_groups: BigCommerceCustomerGroupsAPI = BigCommerceCustomerGroupsAPI(store_hash, access_token)
        self.customers: BigCommerceCustomersAPI = BigCommerceCustomersAPI(store_hash, access_token)
        self.orders: BigCommerceOrdersAPI = BigCommerceOrdersAPI(store_hash, access_token)
        self.products: BigCommerceProductsAPI = BigCommerceProductsAPI(store_hash, access_token)
        self.product_variants: BigCommerceProductVariantsAPI = BigCommerceProductVariantsAPI(store_hash, access_token)
        self.webhooks: BigCommerceWebhooksAPI = BigCommerceWebhooksAPI(store_hash, access_token)
