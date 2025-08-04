from typing import *

from pydantic import BaseModel, Field


class V2fbsPostingProductCountrySetResponse(BaseModel):
    """
    object model
    """

    product_id: Optional[int] = Field(alias="product_id", default=None)

    is_gtd_needed: Optional[bool] = Field(alias="is_gtd_needed", default=None)
