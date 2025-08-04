from enum import Enum


class V1supplyOrderCancelStatusResponseStatus(str, Enum):

    SUCCESS = "SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    ERROR = "ERROR"
