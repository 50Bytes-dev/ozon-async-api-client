from typing import *

from pydantic import BaseModel, Field


class DraftSupplyCreateStatusResponseResult(BaseModel):
    """
    None model

    Идентификаторы заявок на поставку.
    """

    order_ids: Optional[List[int]] = Field(alias="order_ids", default=None)
