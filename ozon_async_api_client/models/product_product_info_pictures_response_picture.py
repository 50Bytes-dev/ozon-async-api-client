from typing import *

from pydantic import BaseModel, Field


class ProductProductInfoPicturesResponsePicture(BaseModel):
    """
    object model
    """

    is_360: Optional[bool] = Field(alias="is_360", default=None)

    is_color: Optional[bool] = Field(alias="is_color", default=None)

    is_primary: Optional[bool] = Field(alias="is_primary", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    url: Optional[str] = Field(alias="url", default=None)
