from typing import *

from pydantic import BaseModel, Field


class V1questionListResponseQuestions(BaseModel):
    """
    object model
    """

    answers_count: Optional[int] = Field(alias="answers_count", default=None)

    author_name: Optional[str] = Field(alias="author_name", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    product_url: Optional[str] = Field(alias="product_url", default=None)

    published_at: Optional[str] = Field(alias="published_at", default=None)

    question_link: Optional[str] = Field(alias="question_link", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    text: Optional[str] = Field(alias="text", default=None)
