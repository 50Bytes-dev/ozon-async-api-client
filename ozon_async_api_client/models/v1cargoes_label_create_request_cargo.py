from typing import *

from pydantic import BaseModel, Field


class V1cargoesLabelCreateRequestCargo(BaseModel):
    """
    None model
    """

    cargo_id: Optional[int] = Field(alias="cargo_id", default=None)
