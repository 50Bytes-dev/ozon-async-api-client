from enum import Enum


class AverageDeliveryTimeSummaryResponseTariffStatus(str, Enum):

    TARIFFSTATUS_UNSPECIFIED = "TariffStatus_Unspecified"
    GOOD = "GOOD"
    MEDIUM = "MEDIUM"
    BAD = "BAD"
