from typing import *

from pydantic import BaseModel, Field


class V1searchAttributeValuesRequest(BaseModel):
    """
    object model
    """

    attribute_id: int = Field(alias="attribute_id")

    description_category_id: int = Field(alias="description_category_id")

    limit: int = Field(alias="limit")

    type_id: int = Field(alias="type_id")

    value: str = Field(alias="value")
