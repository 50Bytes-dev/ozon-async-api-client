from typing import *

from pydantic import BaseModel, Field


class V1productUpdateAttributesRequestAttribute(BaseModel):
    """
    object model
    """

    complex_id: Optional[int] = Field(alias="complex_id", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    values: Optional[Any] = Field(alias="values", default=None)
