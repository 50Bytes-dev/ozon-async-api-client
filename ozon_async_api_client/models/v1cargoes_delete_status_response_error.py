from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_delete_status_response_error_cargo_error_reason import \
    V1cargoesDeleteStatusResponseErrorCargoErrorReason
from .v1cargoes_delete_status_response_error_supply_error_reason_enum import \
    V1cargoesDeleteStatusResponseErrorSupplyErrorReasonEnum


class V1cargoesDeleteStatusResponseError(BaseModel):
    """
    None model

    Список ошибок, которые возникли при удалении грузомест.
    """

    cargo_error_reasons: Optional[List[Optional[V1cargoesDeleteStatusResponseErrorCargoErrorReason]]] = Field(
        alias="cargo_error_reasons", default=None
    )

    supply_error_reasons: Optional[List[Optional[V1cargoesDeleteStatusResponseErrorSupplyErrorReasonEnum]]] = Field(
        alias="supply_error_reasons", default=None
    )
