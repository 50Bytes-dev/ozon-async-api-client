from enum import Enum


class V1getSupplyOrderTimeslotStatusResponseStatus(str, Enum):

    STATUS_UNSPECIFIED = "STATUS_UNSPECIFIED"
    STATUS_ERROR = "STATUS_ERROR"
    STATUS_IN_PROGRESS = "STATUS_IN_PROGRESS"
    STATUS_SUCCESS = "STATUS_SUCCESS"
