from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerCreateRequest(BaseModel):
    """
    object model
    """

    question_id: Union[str, int] = Field(alias="question_id")

    sku: int = Field(alias="sku")

    text: str = Field(alias="text")
