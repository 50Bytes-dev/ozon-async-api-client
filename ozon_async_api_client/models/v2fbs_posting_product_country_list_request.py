from typing import *

from pydantic import BaseModel, Field


class V2fbsPostingProductCountryListRequest(BaseModel):
    """
    object model
    """

    name_search: Optional[str] = Field(alias="name_search", default=None)
