from typing import *

from pydantic import BaseModel, Field


class ProductGetProductInfoDescriptionResponseProduct(BaseModel):
    """
    object model
    """

    description: Optional[str] = Field(alias="description", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)
