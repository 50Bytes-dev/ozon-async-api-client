from typing import *

from pydantic import BaseModel, Field

from .v2create_label_batch_response_result import V2createLabelBatchResponseResult


class V2createLabelBatchResponse(BaseModel):
    """
    object model
    """

    result: Optional[V2createLabelBatchResponseResult] = Field(alias="result", default=None)
