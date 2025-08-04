from typing import *

from pydantic import BaseModel, Field


class V2postingFBSGetDigitalActRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

    doc_type: Optional[Any] = Field(alias="doc_type", default=None)
