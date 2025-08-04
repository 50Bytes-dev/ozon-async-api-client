from typing import *

from pydantic import BaseModel, Field


class V1draftClusterListResponseWarehouse(BaseModel):
    """
    None model
    """

    name: Optional[str] = Field(alias="name", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
