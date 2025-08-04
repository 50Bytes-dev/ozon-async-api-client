from typing import *

from pydantic import BaseModel, Field


class V1questionChangeStatusRequest(BaseModel):
    """
    object model
    """

    question_ids: Any = Field(alias="question_ids")

    status: str = Field(alias="status")
