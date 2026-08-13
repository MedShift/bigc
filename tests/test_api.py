import threading

from bigc import BigCommerceAPI


class TestSession:
    def test_api_versions_share_one_session(self):
        api = BigCommerceAPI('store_hash', 'access_token')

        assert api.api_v2._session is api.api_v3._session

    def test_each_thread_gets_its_own_session(self):
        api = BigCommerceAPI('store_hash', 'access_token')
        sessions = []

        threads = [threading.Thread(target=lambda: sessions.append(api.api_v2._session)) for _ in range(8)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        assert len(sessions) == len(threads)
        assert len(set(sessions)) == len(threads)
        assert api.api_v2._session not in sessions
