from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_label_create_errors import V1cargoesLabelCreateErrors
from .v1cargoes_label_get_response_result import V1cargoesLabelGetResponseResult
from .v1cargoes_label_get_response_status import V1cargoesLabelGetResponseStatus


class V1cargoesLabelGetResponse(BaseModel):
    """
    None model
    """

    result: Optional[V1cargoesLabelGetResponseResult] = Field(alias="result", default=None)

    status: Optional[V1cargoesLabelGetResponseStatus] = Field(alias="status", default=None)

    errors: Optional[V1cargoesLabelCreateErrors] = Field(alias="errors", default=None)
