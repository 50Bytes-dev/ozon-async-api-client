from typing import *

from pydantic import BaseModel, Field

from .v2hs_code import V2hsCode


class InvoiceGetV2responseResult(BaseModel):
    """
    object model

    Информация о счёте-фактуре.
    """

    date: Optional[str] = Field(alias="date", default=None)

    file_url: Optional[str] = Field(alias="file_url", default=None)

    hs_codes: Optional[List[Optional[V2hsCode]]] = Field(alias="hs_codes", default=None)

    number: Optional[str] = Field(alias="number", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    price_currency: Optional[str] = Field(alias="price_currency", default=None)
