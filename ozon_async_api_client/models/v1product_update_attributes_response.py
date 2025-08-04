from typing import *

from pydantic import BaseModel, Field


class V1productUpdateAttributesResponse(BaseModel):
    """
    object model
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)
