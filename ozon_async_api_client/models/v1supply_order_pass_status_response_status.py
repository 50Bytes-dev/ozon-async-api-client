from enum import Enum


class V1supplyOrderPassStatusResponseStatus(str, Enum):

    UNKNOWN = "Unknown"
    SUCCESS = "Success"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
