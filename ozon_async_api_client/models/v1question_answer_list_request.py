from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerListRequest(BaseModel):
    """
    object model
    """

    last_id: Optional[Any] = Field(alias="last_id", default=None)

    question_id: str = Field(alias="question_id")

    sku: int = Field(alias="sku")
