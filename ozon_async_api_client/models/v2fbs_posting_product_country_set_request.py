from typing import *

from pydantic import BaseModel, Field


class V2fbsPostingProductCountrySetRequest(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")

    product_id: int = Field(alias="product_id")

    country_iso_code: str = Field(alias="country_iso_code")
