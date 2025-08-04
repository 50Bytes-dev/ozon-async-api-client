from typing import *

from pydantic import BaseModel, Field


class ProductCertificationListResponseCertification(BaseModel):
    """
    object model
    """

    category_name: Optional[str] = Field(alias="category_name", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)
