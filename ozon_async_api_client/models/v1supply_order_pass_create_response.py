from typing import *

from pydantic import BaseModel, Field

from .v1set_vehicle_error import V1setVehicleError


class V1supplyOrderPassCreateResponse(BaseModel):
    """
    object model
    """

    error_reasons: Optional[List[Optional[V1setVehicleError]]] = Field(alias="error_reasons", default=None)

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
