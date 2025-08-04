from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_delete_status_response_error_cargo_error_reason_error_reason_enum import \
    V1cargoesDeleteStatusResponseErrorCargoErrorReasonErrorReasonEnum


class V1cargoesDeleteStatusResponseErrorCargoErrorReason(BaseModel):
    """
    None model
    """

    cargo_id: Optional[int] = Field(alias="cargo_id", default=None)

    error_reasons: Optional[List[Optional[V1cargoesDeleteStatusResponseErrorCargoErrorReasonErrorReasonEnum]]] = Field(
        alias="error_reasons", default=None
    )
