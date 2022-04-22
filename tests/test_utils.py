from datetime import datetime, timedelta, timezone
import pytest
from bigc.utils import parse_rfc2822_date

TZ_UTC = timezone.utc


class TestParseRfc2822Date:
    @pytest.mark.parametrize('test_input,expected', [
        ('Mon, 01 Jan 1900 00:00:00 +0000', datetime(1900, 1, 1, tzinfo=TZ_UTC)),
        ('1 Jan 1900 00:00 +0000', datetime(1900, 1, 1, tzinfo=TZ_UTC)),
        ('Sun, 20 Jul 1969 20:17:40 +0000', datetime(1969, 7, 20, 20, 17, 40, tzinfo=TZ_UTC)),
        ('Tue, 05 Mar 2019 21:40:11 +0000', datetime(2019, 3, 5, 21, 40, 11, tzinfo=TZ_UTC)),
    ])
    def test_parse_utc(self, test_input, expected):
        assert parse_rfc2822_date(test_input) == expected

    @pytest.mark.parametrize('test_input,expected', [
        ('Sat, 01 Jan 2000 0:00:00 +0000', datetime(2000, 1, 1, tzinfo=TZ_UTC)),
        ('Sat, 01 Jan 2000 0:00:00 -0400', datetime(2000, 1, 1, tzinfo=timezone(-timedelta(hours=4)))),
        ('Sat, 01 Jan 2000 0:00:00 +0900', datetime(2000, 1, 1, tzinfo=timezone(timedelta(hours=9)))),
    ])
    def test_parse_tz(self, test_input, expected):
        assert parse_rfc2822_date(test_input) == expected
        assert parse_rfc2822_date(test_input).tzinfo == TZ_UTC
