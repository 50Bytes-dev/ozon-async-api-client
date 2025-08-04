from typing import *

from pydantic import BaseModel, Field


class GetProductRatingBySkuResponseRatingGroup(BaseModel):
    """
    object model
    """

    conditions: Optional[Any] = Field(alias="conditions", default=None)

    improve_at_least: Optional[int] = Field(alias="improve_at_least", default=None)

    improve_attributes: Optional[Any] = Field(alias="improve_attributes", default=None)

    key: Optional[Union[str, int]] = Field(alias="key", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    rating: Optional[float] = Field(alias="rating", default=None)

    weight: Optional[float] = Field(alias="weight", default=None)
