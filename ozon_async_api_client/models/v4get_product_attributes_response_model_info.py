from typing import *

from pydantic import BaseModel, Field


class V4getProductAttributesResponseModelInfo(BaseModel):
    """
    object model

    Информация о модели.
    """

    model_id: Optional[int] = Field(alias="model_id", default=None)

    count: Optional[int] = Field(alias="count", default=None)
