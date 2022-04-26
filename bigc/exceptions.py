class BigCommerceAPIException(Exception):
    """Base exception class for BigCommerce API errors"""


class BigCommerceRedirectionError(BigCommerceAPIException):
    """Exception class for 3xx errors from the BigCommerce API."""


class BigCommerceClientError(BigCommerceAPIException):
    """
    Exception class for 4xx errors from the BigCommerce API.

    This indicates a client-side error, and the request should not be retried.
    """


class BadRequestError(BigCommerceAPIException):
    """The request was malformed in some way"""


class InvalidAuthorizationError(BigCommerceClientError):
    """An access token was not provided, or it is not valid on the storefront used"""


class InsufficientScopesError(BigCommerceClientError):
    """The access token used does not have the required permissions for the operation"""


class ResourceNotFoundError(BigCommerceClientError):
    """The requested resource does not exist"""


class RateLimitExceededError(BigCommerceClientError):
    """The OAuth client has exceeded the storefront's rate limit"""


class BigCommerceServerError(BigCommerceAPIException):
    """
    Exception class for 5xx errors from the BigCommerce API.

    This indicates a server-side error, and the request may succeed if retried later.
    """


class InternalBigCommerceError(BigCommerceServerError):
    """An error has occurred within the BigCommerce API"""


class StoreUnavailableError(BigCommerceServerError):
    """The store is currently offline or suspended"""


class PlanLimitExceededError(BigCommerceServerError):
    """The store has exceeded the BigCommerce plan's limit for a resource"""
