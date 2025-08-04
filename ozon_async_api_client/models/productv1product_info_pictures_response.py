from typing import *

from pydantic import BaseModel, Field

from .productv1product_info_pictures_response_result import Productv1productInfoPicturesResponseResult


class Productv1productInfoPicturesResponse(BaseModel):
    """
    object model
    """

    result: Optional[Productv1productInfoPicturesResponseResult] = Field(alias="result", default=None)
