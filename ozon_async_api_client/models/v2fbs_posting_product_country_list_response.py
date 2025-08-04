from typing import *

from pydantic import BaseModel, Field

from .v2fbs_posting_product_country_list_response_result import V2fbsPostingProductCountryListResponseResult


class V2fbsPostingProductCountryListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V2fbsPostingProductCountryListResponseResult]]] = Field(alias="result", default=None)
