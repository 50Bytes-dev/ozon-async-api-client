from typing import *

from pydantic import BaseModel, Field


class ProductImportProductsBySKUResponseResult(BaseModel):
    """
    object model
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)

    unmatched_sku_list: Optional[List[int]] = Field(alias="unmatched_sku_list", default=None)
