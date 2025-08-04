from typing import *

from pydantic import BaseModel, Field


class V1statusCodeNamePairRejection(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    name: Optional[str] = Field(alias="name", default=None)
