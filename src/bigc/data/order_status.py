from enum import IntEnum, unique


@unique
class BigCommerceOrderStatus(IntEnum):
    """Enum mapping BigCommerce order statuses to their IDs"""
    INCOMPLETE = 0
    PENDING = 1
    SHIPPED = 2
    PARTIALLY_SHIPPED = 3
    REFUNDED = 4
    CANCELLED = 5
    DECLINED = 6
    AWAITING_PAYMENT = 7
    AWAITING_PICKUP = 8
    AWAITING_SHIPMENT = 9
    COMPLETED = 10
    AWAITING_FULFILLMENT = 11
    MANUAL_VERIFICATION_REQUIRED = 12
    DISPUTED = 13
    PARTIALLY_REFUNDED = 14
