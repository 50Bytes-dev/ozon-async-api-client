from typing import *

from pydantic import BaseModel, Field


class Postingv3fbsPostingWithParams(BaseModel):
    """
    object model

    Дополнительные поля, которые нужно добавить в ответ.
    """

    analytics_data: Optional[bool] = Field(alias="analytics_data", default=None)

    barcodes: Optional[bool] = Field(alias="barcodes", default=None)

    financial_data: Optional[bool] = Field(alias="financial_data", default=None)

    legal_info: Optional[bool] = Field(alias="legal_info", default=None)

    translit: Optional[bool] = Field(alias="translit", default=None)
