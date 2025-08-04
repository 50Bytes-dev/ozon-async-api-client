from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_delete_response_error_cargo_error_reason import V1cargoesDeleteResponseErrorCargoErrorReason
from .v1cargoes_delete_response_error_supply_error_reason_enum import V1cargoesDeleteResponseErrorSupplyErrorReasonEnum


class V1cargoesDeleteResponseError(BaseModel):
    """
    None model

    Список ошибок, которые возникли при удалении грузомест.
    """

    cargo_error_reasons: Optional[List[Optional[V1cargoesDeleteResponseErrorCargoErrorReason]]] = Field(
        alias="cargo_error_reasons", default=None
    )

    supply_error_reasons: Optional[List[Optional[V1cargoesDeleteResponseErrorSupplyErrorReasonEnum]]] = Field(
        alias="supply_error_reasons", default=None
    )
