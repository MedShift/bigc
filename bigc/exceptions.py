from __future__ import annotations

from typing import Optional

from requests import Response


class BigCommerceAPIException(Exception):
    """Base exception class for BigCommerce API errors"""

    def __init__(self, message: Optional[str] = None, response: Optional[Response] = None):
        self._message = message
        self.response = response

        super().__init__(
            message or f'Request to BigCommerce failed{f" with {self.message}" if response is not None else ""}'
        )

    @property
    def status_code(self) -> Optional[int]:
        if self.response is None:
            return None

        return self.response.status_code

    @property
    def message(self) -> str:
        if self._message is not None:
            return self._message

        return f'{self.status_code} {self.response.reason}: {self.response.text}'


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
