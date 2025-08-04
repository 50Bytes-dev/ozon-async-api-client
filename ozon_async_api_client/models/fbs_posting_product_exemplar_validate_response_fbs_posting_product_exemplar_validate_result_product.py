from typing import *

from pydantic import BaseModel, Field


class FbsPostingProductExemplarValidateResponseFbsPostingProductExemplarValidateResultProduct(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    exemplars: Optional[Any] = Field(alias="exemplars", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    valid: Optional[bool] = Field(alias="valid", default=None)
