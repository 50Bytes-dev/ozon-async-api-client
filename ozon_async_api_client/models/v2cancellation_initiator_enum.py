from enum import Enum


class V2cancellationInitiatorEnum(str, Enum):

    OZON = "OZON"
    SELLER = "SELLER"
    CLIENT = "CLIENT"
    SYSTEM = "SYSTEM"
    DELIVERY = "DELIVERY"
