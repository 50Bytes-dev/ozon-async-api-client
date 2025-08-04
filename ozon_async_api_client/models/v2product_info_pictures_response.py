from typing import *

from pydantic import BaseModel, Field

from .v2product_info_pictures_response_item import V2productInfoPicturesResponseItem


class V2productInfoPicturesResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V2productInfoPicturesResponseItem]]] = Field(alias="items", default=None)
