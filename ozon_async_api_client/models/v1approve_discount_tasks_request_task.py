from typing import *

from pydantic import BaseModel, Field


class V1approveDiscountTasksRequestTask(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

    approved_price: float = Field(alias="approved_price")

    seller_comment: Optional[str] = Field(alias="seller_comment", default=None)

    approved_quantity_min: int = Field(alias="approved_quantity_min")

    approved_quantity_max: int = Field(alias="approved_quantity_max")
