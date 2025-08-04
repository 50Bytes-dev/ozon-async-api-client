from typing import *

from pydantic import BaseModel, Field

from .v2product_info_pictures_response_error import V2productInfoPicturesResponseError


class V2productInfoPicturesResponseItem(BaseModel):
    """
    object model
    """

    product_id: Optional[int] = Field(alias="product_id", default=None)

    primary_photo: Optional[List[str]] = Field(alias="primary_photo", default=None)

    photo: Optional[List[str]] = Field(alias="photo", default=None)

    color_photo: Optional[List[str]] = Field(alias="color_photo", default=None)

    photo_360: Optional[List[str]] = Field(alias="photo_360", default=None)

    errors: Optional[List[Optional[V2productInfoPicturesResponseError]]] = Field(alias="errors", default=None)
