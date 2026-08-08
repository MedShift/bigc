from bigc import BigCommerceAPI


class TestSession:
    def test_api_versions_share_one_session(self):
        api = BigCommerceAPI('store_hash', 'access_token')

        assert api.api_v2.session is api.session
        assert api.api_v3.session is api.session
