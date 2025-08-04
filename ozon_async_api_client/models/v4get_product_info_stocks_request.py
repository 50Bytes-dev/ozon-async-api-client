from typing import *

from pydantic import BaseModel, Field

from .v4get_product_info_stocks_request_filter import V4getProductInfoStocksRequestFilter


class V4getProductInfoStocksRequest(BaseModel):
    """
    None model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    filter: V4getProductInfoStocksRequestFilter = Field(alias="filter")

    limit: int = Field(alias="limit")
