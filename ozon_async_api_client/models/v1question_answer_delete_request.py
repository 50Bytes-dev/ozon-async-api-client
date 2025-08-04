from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerDeleteRequest(BaseModel):
    """
    object model
    """

    answer_id: Union[str, int] = Field(alias="answer_id")

    sku: int = Field(alias="sku")
