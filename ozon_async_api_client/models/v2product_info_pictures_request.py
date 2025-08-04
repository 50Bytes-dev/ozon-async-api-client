from typing import *

from pydantic import BaseModel, Field


class V2productInfoPicturesRequest(BaseModel):
    """
    object model
    """

    product_id: Any = Field(alias="product_id")
