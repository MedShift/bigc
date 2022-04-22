from datetime import datetime, timezone
from email.utils import parsedate_tz, mktime_tz

__all__ = ('parse_rfc2822_date',)


# The BigCommerce API uses RFC-2822 sometimes, and there isn't a one-liner
# in the standard library to parse it.
def parse_rfc2822_date(date_str: str) -> datetime:
    """Parse an RFC-2822 date using ``email.utils.parsedate_tz`` and return a ``datetime`` instance"""
    parsed_parts: tuple = parsedate_tz(date_str)
    utc_timestamp: int = mktime_tz(parsed_parts)
    return datetime.fromtimestamp(utc_timestamp, tz=timezone.utc)
