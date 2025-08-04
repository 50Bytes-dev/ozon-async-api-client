from typing import *

from pydantic import BaseModel, Field


class ProductCertificateUnbindResponseItem(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    updated: Optional[bool] = Field(alias="updated", default=None)
