from typing import *

from pydantic import BaseModel, Field


class V1cargoesRulesGetRequest(BaseModel):
    """
    None model
    """

    supply_ids: Optional[List[int]] = Field(alias="supply_ids", default=None)
