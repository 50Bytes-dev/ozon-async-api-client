from typing import *

from pydantic import BaseModel, Field


class V1cargoesDeleteRequest(BaseModel):
    """
    None model
    """

    cargo_ids: Optional[List[int]] = Field(alias="cargo_ids", default=None)

    supply_id: Optional[int] = Field(alias="supply_id", default=None)
