from typing import *

from pydantic import BaseModel, Field

from .cargoes_create_errors_error_reason import CargoesCreateErrorsErrorReason
from .cargoes_create_errors_item_validation import CargoesCreateErrorsItemValidation


class V1cargoesCreateErrors(BaseModel):
    """
    None model

    Ошибки.
    """

    error_reasons: Optional[List[Optional[CargoesCreateErrorsErrorReason]]] = Field(alias="error_reasons", default=None)

    items_validation: Optional[List[Optional[CargoesCreateErrorsItemValidation]]] = Field(
        alias="items_validation", default=None
    )
