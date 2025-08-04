from enum import Enum


class V1averageDeliveryTimeDetailsResponseDeliveryTimeStatus(str, Enum):

    UNKNOWN = "UNKNOWN"
    FAST = "FAST"
    MEDIUM = "MEDIUM"
    LONG = "LONG"
