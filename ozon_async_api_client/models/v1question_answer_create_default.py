from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerCreateDefault(BaseModel):
    """
    object model
    """

    code: Optional[int] = Field(alias="code", default=None)

    details: Optional[str] = Field(alias="details", default=None)

    message: Optional[str] = Field(alias="message", default=None)
