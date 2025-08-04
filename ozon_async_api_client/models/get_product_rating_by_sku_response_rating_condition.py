from typing import *

from pydantic import BaseModel, Field


class GetProductRatingBySkuResponseRatingCondition(BaseModel):
    """
    object model
    """

    cost: Optional[float] = Field(alias="cost", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    fulfilled: Optional[bool] = Field(alias="fulfilled", default=None)

    key: Optional[Union[str, int]] = Field(alias="key", default=None)
