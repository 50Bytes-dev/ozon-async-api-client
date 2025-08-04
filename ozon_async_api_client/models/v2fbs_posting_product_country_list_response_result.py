from typing import *

from pydantic import BaseModel, Field


class V2fbsPostingProductCountryListResponseResult(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    country_iso_code: Optional[str] = Field(alias="country_iso_code", default=None)
