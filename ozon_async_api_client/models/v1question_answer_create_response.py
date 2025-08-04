from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerCreateResponse(BaseModel):
    """
    object model
    """

    answer_id: Optional[str] = Field(alias="answer_id", default=None)
