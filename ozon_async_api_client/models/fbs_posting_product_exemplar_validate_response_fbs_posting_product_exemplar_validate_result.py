from typing import *

from pydantic import BaseModel, Field


class FbsPostingProductExemplarValidateResponseFbsPostingProductExemplarValidateResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    products: Optional[Any] = Field(alias="products", default=None)
