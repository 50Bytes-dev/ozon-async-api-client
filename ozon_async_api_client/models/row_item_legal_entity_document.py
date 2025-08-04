from typing import *

from pydantic import BaseModel, Field


class RowItemLegalEntityDocument(BaseModel):
    """
    object model

    Информация о продаже юридическому лицу.
    """

    number: Optional[str] = Field(alias="number", default=None)

    sale_date: Optional[str] = Field(alias="sale_date", default=None)
