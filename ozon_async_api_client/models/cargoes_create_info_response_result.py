from typing import *

from pydantic import BaseModel, Field

from .cargoes_create_info_response_result_cargo import CargoesCreateInfoResponseResultCargo


class CargoesCreateInfoResponseResult(BaseModel):
    """
    None model

    Результат запроса.
    """

    cargoes: Optional[List[Optional[CargoesCreateInfoResponseResultCargo]]] = Field(alias="cargoes", default=None)
