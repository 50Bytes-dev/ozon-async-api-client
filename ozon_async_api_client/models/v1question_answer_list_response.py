from typing import *

from pydantic import BaseModel, Field


class V1questionAnswerListResponse(BaseModel):
    """
    object model
    """

    answers: Optional[Any] = Field(alias="answers", default=None)

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)
