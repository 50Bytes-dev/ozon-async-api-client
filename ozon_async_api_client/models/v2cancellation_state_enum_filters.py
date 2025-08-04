from enum import Enum


class V2cancellationStateEnumFilters(str, Enum):

    ALL = "ALL"
    ON_APPROVAL = "ON_APPROVAL"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
