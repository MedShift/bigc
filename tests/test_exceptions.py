import pytest

from bigc.exceptions import *


class TestBigCommerceException:
    def test_str(self):
        error_msg = 'Something went wrong!'
        assert str(BigCommerceException(error_msg)) == error_msg
        assert str(DoesNotExistError(error_msg)) == error_msg
        assert str(InternalServerError(error_msg)) == error_msg

    def test_str_default_message(self):
        assert str(BigCommerceException()) == 'Request to BigCommerce failed.'
        assert str(DoesNotExistError()) == 'The requested entity does not exist.'
        assert str(InternalServerError()) == 'An error has occurred within the BigCommerce server.'

    @pytest.mark.parametrize('status_code, exc_class', [
        (301, BigCommerceException),
        (400, BadRequestError),
        (401, UnauthorizedError),
        (403, ForbiddenError),
        (404, DoesNotExistError),
        (405, BigCommerceClientError),
        (406, BigCommerceClientError),
        (409, ConflictError),
        (413, EntityTooLargeError),
        (415, BigCommerceClientError),
        (422, InvalidDataError),
        (423, LockedError),
        (429, TooManyRequestsError),
        (499, BigCommerceClientError),
        (500, InternalServerError),
        (501, BigCommerceServerError),
        (502, BadGatewayError),
        (503, ServiceUnavailableError),
        (504, GatewayTimeoutError),
        (507, InsufficientStorageError),
    ])
    def test_get_exc_class_for_status_code(self, status_code, exc_class):
        assert BigCommerceException.get_exc_class_for_status_code(status_code) is exc_class


class TestBigCommerceExceptionExtractErrorMessage:
    def test_parse_object_style_message(self):
        message, errors = BigCommerceException.extract_error_message({
            'status': 422,
            'title': 'Missing Required Fields',
            'type': 'https://developer.bigcommerce.com/api-docs/getting-started/api-status-codes',
            'errors': {
                'name': 'Please provide a name.',
                'price': 'Please provide a price.',
                'type': 'Please provide a type.',
                'weight': 'Please provide a weight.',
            },
        })

        assert message == 'Missing Required Fields'
        assert errors == {
            'name': 'Please provide a name.',
            'price': 'Please provide a price.',
            'type': 'Please provide a type.',
            'weight': 'Please provide a weight.',
        }

    def test_parse_object_style_message_without_errors(self):
        message, errors = BigCommerceException.extract_error_message({
            'status': 409,
            'title': 'Your checkout could not be processed because some details have changed.',
            'type': 'https://developer.bigcommerce.com/api-docs/getting-started/api-status-codes'
        })

        assert message == 'Your checkout could not be processed because some details have changed.'
        assert errors is None

    def test_parse_object_style_message_without_title(self):
        message, errors = BigCommerceException.extract_error_message({
            'status': 404,
            'type': 'https://developer.bigcommerce.com/api-docs/getting-started/api-status-codes',
        })

        assert message is None
        assert errors is None

    def test_parse_array_style_message(self):
        message, errors = BigCommerceException.extract_error_message([
            {
                'status': 400,
                'message': "The required field 'name' was not supplied.",
            },
        ])

        assert message == "The required field 'name' was not supplied."
        assert errors is None
