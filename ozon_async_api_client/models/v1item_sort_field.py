from enum import Enum


class V1itemSortField(str, Enum):

    UNSPECIFIED = "UNSPECIFIED"
    SKU = "SKU"
    NAME = "NAME"
    QUANTITY = "QUANTITY"
    TOTAL_VOLUME_IN_LITRES = "TOTAL_VOLUME_IN_LITRES"
