from typing import *

from pydantic import BaseModel, Field


class GetProductInfoListResponseStocksStock(BaseModel):
    """
    object model
    """

    present: Optional[int] = Field(alias="present", default=None)

    reserved: Optional[int] = Field(alias="reserved", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    source: Optional[str] = Field(alias="source", default=None)
