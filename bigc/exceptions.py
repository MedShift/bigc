from __future__ import annotations

import inspect
from typing import Any, ClassVar

_status_code_exc_class_map: dict[int, type[BigCommerceException]] = {}


class BigCommerceException(Exception):
    """Base exception class for BigCommerce API errors."""

    DEFAULT_MESSAGE: ClassVar[str] = 'Request to BigCommerce failed.'
    STATUS_CODE: ClassVar[int | None] = None

    def __init__(self,
                 message: str | None = None,
                 status_code: int | None = None,
                 response: Any = None,
                 errors: dict[str, str] | None = None):
        """
        :param message: A short description of the error's cause.
        :param status_code: The HTTP status code of the API response.
        :param response: The underlying API response, if any, that caused the
            error. Currently, this is a ``requests.Response``, but this is an
            implementation detail that's subject to change.
        :param errors: A dictionary that may contain additional error details.
        """
        super().__init__(message, status_code, response, errors)

        self.message = message
        self.status_code = status_code
        self.response = response
        self.errors = errors

    def __str__(self):
        return self.message or self.DEFAULT_MESSAGE

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Only include subclasses defined in this file
        if inspect.getmodule(cls).__name__ == __name__:
            if cls.STATUS_CODE is not None:
                _status_code_exc_class_map[cls.STATUS_CODE] = cls

    @staticmethod
    def get_exc_class_for_status_code(status_code: int) -> type[BigCommerceException]:
        try:
            return _status_code_exc_class_map[status_code]
        except KeyError:
            if 400 <= status_code < 500:
                return BigCommerceClientError
            if 500 <= status_code < 600:
                return BigCommerceServerError
            return BigCommerceException

    @staticmethod
    def extract_error_message(response_data: object) -> tuple[str | None, dict[str, str] | None]:
        message: str | None = None
        errors: dict[str, str] | None = None

        # Object-style error messages
        if isinstance(response_data, dict):
            message = response_data.get('title')
            errors = response_data.get('errors')
        # Array-style error messages
        elif isinstance(response_data, list) and len(response_data) > 0:
            if isinstance(response_data[0], dict):
                message = response_data[0].get('message')

        return message, errors


class BigCommerceClientError(BigCommerceException):
    """Exception class for 4xx errors from the BigCommerce API."""


class BadRequestError(BigCommerceException):
    DEFAULT_MESSAGE = 'The request was malformed in some way.'
    STATUS_CODE = 400


class UnauthorizedError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'Credentials were not provided or are invalid.'
    STATUS_CODE = 401


class ForbiddenError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'The request had insufficient permissions for this operation.'
    STATUS_CODE = 403


class DoesNotExistError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'The requested entity does not exist.'
    STATUS_CODE = 404


class ConflictError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'The requested change has been rejected by BigCommerce.'
    STATUS_CODE = 409


class EntityTooLargeError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'Too many objects were requested.'
    STATUS_CODE = 413


class InvalidDataError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'The request omitted required fields or contained invalid data.'
    STATUS_CODE = 422


class LockedError(BigCommerceClientError):
    DEFAULT_MESSAGE = 'The requested resource is currently unavailable.'
    STATUS_CODE = 423


class TooManyRequestsError(BigCommerceClientError):
    DEFAULT_MESSAGE = "The store's rate limit has been exceeded."
    STATUS_CODE = 429


class BigCommerceServerError(BigCommerceException):
    """Exception class for 5xx errors from the BigCommerce API."""


class InternalServerError(BigCommerceServerError):
    DEFAULT_MESSAGE = 'An error has occurred within the BigCommerce server.'
    STATUS_CODE = 500


class BadGatewayError(BigCommerceServerError):
    DEFAULT_MESSAGE = 'Bad gateway.'
    STATUS_CODE = 502


class ServiceUnavailableError(BigCommerceServerError):
    DEFAULT_MESSAGE = 'The store is currently offline or suspended.'
    STATUS_CODE = 503


class GatewayTimeoutError(BigCommerceServerError):
    DEFAULT_MESSAGE = 'The request has timed out.'
    STATUS_CODE = 504


class InsufficientStorageError(BigCommerceServerError):
    DEFAULT_MESSAGE = "The store has exceeded its plan's limit for a resource."
    STATUS_CODE = 507


class BigCommerceNetworkError(BigCommerceException):
    """Exception class for network-related errors."""


__all__ = (
    'BigCommerceException',
    'BigCommerceClientError',
    'BadRequestError',
    'UnauthorizedError',
    'ForbiddenError',
    'DoesNotExistError',
    'ConflictError',
    'EntityTooLargeError',
    'InvalidDataError',
    'LockedError',
    'TooManyRequestsError',
    'BigCommerceServerError',
    'InternalServerError',
    'BadGatewayError',
    'ServiceUnavailableError',
    'GatewayTimeoutError',
    'InsufficientStorageError',
    'BigCommerceNetworkError',
)
