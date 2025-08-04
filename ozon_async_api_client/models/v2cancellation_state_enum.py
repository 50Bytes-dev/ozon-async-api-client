from enum import Enum


class V2cancellationStateEnum(str, Enum):

    ON_APPROVAL = "ON_APPROVAL"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
