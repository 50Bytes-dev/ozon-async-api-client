from typing import *

from pydantic import BaseModel, Field


class GetProductInfoListResponseModelInfo(BaseModel):
    """
    object model

    Информация о модели товара.
    """

    count: Optional[int] = Field(alias="count", default=None)

    model_id: Optional[int] = Field(alias="model_id", default=None)
