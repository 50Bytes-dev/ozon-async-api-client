from typing import *

from pydantic import BaseModel, Field

from .item_validation_error_type import ItemValidationErrorType


class CargoesCreateErrorsItemValidation(BaseModel):
    """
    None model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    cargo_key: Optional[str] = Field(alias="cargo_key", default=None)

    quant: Optional[int] = Field(alias="quant", default=None)

    type: Optional[ItemValidationErrorType] = Field(alias="type", default=None)
