from typing import *

from pydantic import BaseModel, Field

from .cargoes_create_info_response_result import CargoesCreateInfoResponseResult
from .v1cargoes_create_errors import V1cargoesCreateErrors
from .v1cargoes_create_info_response_status import V1cargoesCreateInfoResponseStatus


class V1cargoesCreateInfoResponse(BaseModel):
    """
    None model
    """

    result: Optional[CargoesCreateInfoResponseResult] = Field(alias="result", default=None)

    status: Optional[V1cargoesCreateInfoResponseStatus] = Field(alias="status", default=None)

    errors: Optional[V1cargoesCreateErrors] = Field(alias="errors", default=None)
