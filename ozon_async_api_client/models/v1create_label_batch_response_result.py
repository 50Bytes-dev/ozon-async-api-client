from typing import *

from pydantic import BaseModel, Field


class V1createLabelBatchResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)
