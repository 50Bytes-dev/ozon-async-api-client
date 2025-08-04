from typing import *

from pydantic import BaseModel, Field

from .v2hs_code import V2hsCode


class V2invoiceCreateOrUpdateV2request(BaseModel):
    """
    object model
    """

    date: str = Field(alias="date")

    hs_codes: Optional[List[Optional[V2hsCode]]] = Field(alias="hs_codes", default=None)

    number: Optional[str] = Field(alias="number", default=None)

    posting_number: str = Field(alias="posting_number")

    price: Optional[float] = Field(alias="price", default=None)

    price_currency: Optional[str] = Field(alias="price_currency", default=None)

    url: str = Field(alias="url")
