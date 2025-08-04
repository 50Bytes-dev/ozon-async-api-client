from typing import *

from pydantic import BaseModel, Field


class V1getAttributesResponseAttribute(BaseModel):
    """
    object model
    """

    category_dependent: Optional[bool] = Field(alias="category_dependent", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    dictionary_id: Optional[int] = Field(alias="dictionary_id", default=None)

    group_id: Optional[int] = Field(alias="group_id", default=None)

    group_name: Optional[str] = Field(alias="group_name", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    is_aspect: Optional[bool] = Field(alias="is_aspect", default=None)

    is_collection: Optional[bool] = Field(alias="is_collection", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    attribute_complex_id: Optional[int] = Field(alias="attribute_complex_id", default=None)

    max_value_count: Optional[int] = Field(alias="max_value_count", default=None)

    complex_is_collection: Optional[bool] = Field(alias="complex_is_collection", default=None)
