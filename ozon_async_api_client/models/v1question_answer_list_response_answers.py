from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerListResponseAnswers(BaseModel):
    """
    object model
    """

    author_name: Optional[str] = Field(alias="author_name", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    published_at: Optional[str] = Field(alias="published_at", default=None)

    question_id: Optional[str] = Field(alias="question_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    text: Optional[str] = Field(alias="text", default=None)
