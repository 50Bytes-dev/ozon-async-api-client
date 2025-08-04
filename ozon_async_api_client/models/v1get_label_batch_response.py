from typing import *

from pydantic import BaseModel, Field

from .v1get_label_batch_response_result import V1getLabelBatchResponseResult


class V1getLabelBatchResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1getLabelBatchResponseResult] = Field(alias="result", default=None)
