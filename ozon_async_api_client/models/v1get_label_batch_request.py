from typing import *

from pydantic import BaseModel, Field


class V1getLabelBatchRequest(BaseModel):
    """
    object model
    """

    task_id: int = Field(alias="task_id")
