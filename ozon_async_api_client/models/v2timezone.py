from typing import *

from pydantic import BaseModel, Field


class V2timezone(BaseModel):
    """
    object model
    """

    iana_name: Optional[str] = Field(alias="iana_name", default=None)

    offset: Optional[str] = Field(alias="offset", default=None)
