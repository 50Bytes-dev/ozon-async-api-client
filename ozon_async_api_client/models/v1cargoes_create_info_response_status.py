from enum import Enum


class V1cargoesCreateInfoResponseStatus(str, Enum):

    SUCCESS = "SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
