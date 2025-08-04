from typing import *

from pydantic import BaseModel, Field


class ProductImportProductsPricesResponseError(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)
