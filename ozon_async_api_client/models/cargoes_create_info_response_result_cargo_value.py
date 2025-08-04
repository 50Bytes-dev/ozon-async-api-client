from typing import *

from pydantic import BaseModel, Field


class CargoesCreateInfoResponseResultCargoValue(BaseModel):
    """
    None model

    Информация о грузоместе.
    """

    cargo_id: Optional[int] = Field(alias="cargo_id", default=None)
