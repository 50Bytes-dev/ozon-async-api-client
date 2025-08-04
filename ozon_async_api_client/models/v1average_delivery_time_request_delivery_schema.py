from enum import Enum


class V1averageDeliveryTimeRequestDeliverySchema(str, Enum):

    ALL = "All"
    FBO = "FBO"
    FBS = "FBS"
    UNKNOWN = "UNKNOWN"
