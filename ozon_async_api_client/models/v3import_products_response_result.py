from typing import *

from pydantic import BaseModel, Field


class V3importProductsResponseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)
