from typing import *

from pydantic import BaseModel, Field


class Productsv1getProductInfoStocksByWarehouseFbsResponse(BaseModel):
    """
    object model
    """

    result: Optional[Any] = Field(alias="result", default=None)
