from enum import Enum, unique


@unique
class BigCommerceShippingMethod(Enum):
    """Enumeration of BigCommerce shipping methods"""

    STANDARD = 'Standard'
    SHIP_BY_WEIGHT = 'Ship By Weight'
    CUSTOM_SHIPMENT = 'Custom Shipment'
