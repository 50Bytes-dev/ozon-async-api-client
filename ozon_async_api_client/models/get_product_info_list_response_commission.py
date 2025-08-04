from typing import *

from pydantic import BaseModel, Field


class GetProductInfoListResponseCommission(BaseModel):
    """
    object model
    """

    delivery_amount: Optional[float] = Field(alias="delivery_amount", default=None)

    percent: Optional[float] = Field(alias="percent", default=None)

    return_amount: Optional[float] = Field(alias="return_amount", default=None)

    sale_schema: Optional[str] = Field(alias="sale_schema", default=None)

    value: Optional[float] = Field(alias="value", default=None)
