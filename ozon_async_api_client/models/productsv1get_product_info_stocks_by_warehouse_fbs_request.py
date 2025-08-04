from typing import *

from pydantic import BaseModel, Field


class Productsv1getProductInfoStocksByWarehouseFbsRequest(BaseModel):
    """
    object model
    """

    sku: Any = Field(alias="sku")
