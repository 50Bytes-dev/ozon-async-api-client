from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_label_create_errors_error_reason import V1cargoesLabelCreateErrorsErrorReason


class V1cargoesLabelCreateErrors(BaseModel):
    """
    None model

    Ошибки.
    """

    error_reasons: Optional[List[Optional[V1cargoesLabelCreateErrorsErrorReason]]] = Field(
        alias="error_reasons", default=None
    )
