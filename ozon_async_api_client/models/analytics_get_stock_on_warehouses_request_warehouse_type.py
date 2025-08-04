from enum import Enum


class AnalyticsGetStockOnWarehousesRequestWarehouseType(str, Enum):

    ALL = "ALL"
    EXPRESS_DARK_STORE = "EXPRESS_DARK_STORE"
    NOT_EXPRESS_DARK_STORE = "NOT_EXPRESS_DARK_STORE"
