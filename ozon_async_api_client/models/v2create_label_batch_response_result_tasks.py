from typing import *

from pydantic import BaseModel, Field


class V2createLabelBatchResponseResultTasks(BaseModel):
    """
    object model
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)

    task_type: Optional[str] = Field(alias="task_type", default=None)
