from typing import *

from pydantic import BaseModel, Field


class V1analyticsTurnoverStocksResponseItem(BaseModel):
    """
    object model
    """

    ads: Optional[float] = Field(alias="ads", default=None)

    current_stock: Optional[int] = Field(alias="current_stock", default=None)

    idc: Optional[float] = Field(alias="idc", default=None)

    idc_grade: Optional[str] = Field(alias="idc_grade", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    turnover: Optional[float] = Field(alias="turnover", default=None)

    turnover_grade: Optional[str] = Field(alias="turnover_grade", default=None)
