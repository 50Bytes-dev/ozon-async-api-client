from typing import *

from pydantic import BaseModel, Field


class ListPostingCodesRequestWithParams(BaseModel):
    """
    None model

    Дополнительные поля, которые нужно добавить в ответ.
    """

    analytics_data: Optional[bool] = Field(alias="analytics_data", default=None)

    financial_data: Optional[bool] = Field(alias="financial_data", default=None)

    legal_info: Optional[bool] = Field(alias="legal_info", default=None)
