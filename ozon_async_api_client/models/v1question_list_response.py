from typing import *

from pydantic import BaseModel, Field


class V1questionListResponse(BaseModel):
    """
    object model
    """

    questions: Optional[Any] = Field(alias="questions", default=None)

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)
