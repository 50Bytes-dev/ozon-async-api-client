from typing import *

from pydantic import BaseModel, Field


class Productv1productImportPicturesRequest(BaseModel):
    """
    object model
    """

    color_image: Optional[str] = Field(alias="color_image", default=None)

    images: Optional[Any] = Field(alias="images", default=None)

    images360: Optional[Any] = Field(alias="images360", default=None)

    product_id: int = Field(alias="product_id")
