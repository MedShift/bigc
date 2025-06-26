from typing import Any, Iterator
from unittest.mock import create_autospec, MagicMock, Mock

import pytest
import requests

from bigc.api_client import BigCommerceRequestClient
from bigc.exceptions import BigCommerceNetworkError


class DummyBigCommerceRequestClient(BigCommerceRequestClient):
    def get_many(
        self,
        path: str,
        *,
        page_size: int | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Iterator[Any]:
        raise NotImplementedError

    def _prepare_url(self, path: str) -> str:
        return f'https://api.example.com/stores/{self.store_hash}/test/{path.lstrip("/")}'


@pytest.fixture
def dummy_request_client() -> DummyBigCommerceRequestClient:
    return DummyBigCommerceRequestClient('store_hash', 'access_token')


@pytest.fixture
def request_mock(monkeypatch):
    mock_response = create_autospec(requests.Response)()

    monkeypatch.setattr(
        'bigc.api_client.requests.request',
        mock := MagicMock(return_value=mock_response),
    )

    return mock


class TestRequest:
    def test_retry_for_always_failing_endpoint(self, request_mock, dummy_request_client):
        request_mock.side_effect = requests.RequestException()

        with pytest.raises(BigCommerceNetworkError):
            dummy_request_client.request('GET', '/test', retries=2)

        assert request_mock.call_count == 3

    def test_retry_eventually_succeeds(self, request_mock, dummy_request_client):
        request_mock.side_effect = (requests.RequestException(), requests.RequestException(), request_mock.return_value)

        dummy_request_client.request('GET', '/test', retries=2)

        assert request_mock.call_count == 3
