from typing import *

from pydantic import BaseModel, Field


class ProductGetImportProductsInfoRequest(BaseModel):
    """
    object model
    """

    task_id: int = Field(alias="task_id")
