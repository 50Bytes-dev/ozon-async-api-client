from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerCreateResponse(BaseModel):
    """
    object model
    """

    answer_id: Optional[Union[str, int]] = Field(alias="answer_id", default=None)
