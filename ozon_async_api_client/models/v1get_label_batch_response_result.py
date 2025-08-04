from typing import *

from pydantic import BaseModel, Field


class V1getLabelBatchResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    error: Optional[str] = Field(alias="error", default=None)

    file_url: Optional[str] = Field(alias="file_url", default=None)

    status: Optional[str] = Field(alias="status", default=None)
