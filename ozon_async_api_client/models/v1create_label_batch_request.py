from typing import *

from pydantic import BaseModel, Field


class V1createLabelBatchRequest(BaseModel):
    """
    object model
    """

    posting_number: Any = Field(alias="posting_number")
