from enum import Enum


class V1averageDeliveryTimeResponseDeliveryTimeStatus(str, Enum):

    UNKNOWN = "UNKNOWN"
    FAST = "FAST"
    MEDIUM = "MEDIUM"
    LONG = "LONG"
