from typing import *

from pydantic import BaseModel, Field

from .v2create_label_batch_response_result_tasks import V2createLabelBatchResponseResultTasks


class V2createLabelBatchResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    tasks: Optional[List[Optional[V2createLabelBatchResponseResultTasks]]] = Field(alias="tasks", default=None)
