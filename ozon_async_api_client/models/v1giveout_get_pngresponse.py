from typing import *

from pydantic import BaseModel, Field


class V1giveoutGetPNGResponse(BaseModel):
    """
    object model
    """

    file_content: Optional[str] = Field(alias="file_content", default=None)

    file_name: Optional[str] = Field(alias="file_name", default=None)

    content_type: Optional[str] = Field(alias="content_type", default=None)
