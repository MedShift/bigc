from enum import Enum, unique


@unique
class BigCommerceShippingProvider(Enum):
    """Enumeration of BigCommerce shipping providers"""

    AUSPOST = 'auspost'
    CANADAPOST = 'canadapost'
    ENDICIA = 'endicia'
    USPS = 'usps'
    FEDEX = 'fedex'
    UPS = 'ups'
    UPSREADY = 'upsready'
    UPSONLINE = 'upsonline'
    SHIPPERHQ = 'shipperhq'
