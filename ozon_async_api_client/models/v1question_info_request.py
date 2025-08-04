from typing import *

from pydantic import BaseModel, Field


class V1questionInfoRequest(BaseModel):
    """
    object model
    """

    question_id: Union[str, int] = Field(alias="question_id")
