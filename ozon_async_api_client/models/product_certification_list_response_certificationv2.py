from typing import *

from pydantic import BaseModel, Field


class ProductCertificationListResponseCertificationv2(BaseModel):
    """
    None model
    """

    category_id: Optional[int] = Field(alias="category_id", default=None)

    category_name: Optional[str] = Field(alias="category_name", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    type_id: Optional[int] = Field(alias="type_id", default=None)

    type_name: Optional[str] = Field(alias="type_name", default=None)
