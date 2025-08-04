from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_delete_response_error import V1cargoesDeleteResponseError


class V1cargoesDeleteResponse(BaseModel):
    """
    None model
    """

    errors: Optional[V1cargoesDeleteResponseError] = Field(alias="errors", default=None)

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
