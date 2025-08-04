from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_delete_response_error_cargo_error_reason_error_reason_enum import \
    V1cargoesDeleteResponseErrorCargoErrorReasonErrorReasonEnum


class V1cargoesDeleteResponseErrorCargoErrorReason(BaseModel):
    """
    None model
    """

    cargo_id: Optional[int] = Field(alias="cargo_id", default=None)

    error_reasons: Optional[List[Optional[V1cargoesDeleteResponseErrorCargoErrorReasonErrorReasonEnum]]] = Field(
        alias="error_reasons", default=None
    )
