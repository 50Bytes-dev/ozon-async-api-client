from typing import *

from pydantic import BaseModel, Field


class ProductInfoWrongVolumeResponseWrongVolumeProduct(BaseModel):
    """
    object model
    """

    height: Optional[int] = Field(alias="height", default=None)

    length: Optional[int] = Field(alias="length", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    weight: Optional[int] = Field(alias="weight", default=None)

    width: Optional[int] = Field(alias="width", default=None)
