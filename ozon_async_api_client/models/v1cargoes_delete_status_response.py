from typing import *

from pydantic import BaseModel, Field

from .cargoes_delete_status_response_status_enum import CargoesDeleteStatusResponseStatusEnum
from .v1cargoes_delete_status_response_error import V1cargoesDeleteStatusResponseError


class V1cargoesDeleteStatusResponse(BaseModel):
    """
    None model
    """

    errors: Optional[V1cargoesDeleteStatusResponseError] = Field(alias="errors", default=None)

    status: Optional[CargoesDeleteStatusResponseStatusEnum] = Field(alias="status", default=None)
