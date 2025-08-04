from typing import *

from pydantic import BaseModel, Field


class GetProductAttributesResponseImage(BaseModel):
    """
    object model
    """

    default: Optional[bool] = Field(alias="default", default=None)

    file_name: Optional[str] = Field(alias="file_name", default=None)

    index: Optional[int] = Field(alias="index", default=None)
