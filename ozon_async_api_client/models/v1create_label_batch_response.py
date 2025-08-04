from typing import *

from pydantic import BaseModel, Field

from .v1create_label_batch_response_result import V1createLabelBatchResponseResult


class V1createLabelBatchResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1createLabelBatchResponseResult] = Field(alias="result", default=None)
