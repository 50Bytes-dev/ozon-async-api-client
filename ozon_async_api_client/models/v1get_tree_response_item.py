from typing import *

from pydantic import BaseModel, Field


class V1getTreeResponseItem(BaseModel):
    """
    object model
    """

    description_category_id: Optional[int] = Field(alias="description_category_id", default=None)

    category_name: Optional[str] = Field(alias="category_name", default=None)

    children: Optional[List[Optional["V1getTreeResponseItem"]]] = Field(alias="children", default=None)

    disabled: Optional[bool] = Field(alias="disabled", default=None)

    type_id: Optional[int] = Field(alias="type_id", default=None)

    type_name: Optional[str] = Field(alias="type_name", default=None)
