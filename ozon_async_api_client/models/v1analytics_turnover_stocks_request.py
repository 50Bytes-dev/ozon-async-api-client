from typing import *

from pydantic import BaseModel, Field


class V1analyticsTurnoverStocksRequest(BaseModel):
    """
    object model
    """

    limit: Optional[int] = Field(alias="limit", default=None)

    offset: Optional[int] = Field(alias="offset", default=None)

    sku: Optional[List[int]] = Field(alias="sku", default=None)
