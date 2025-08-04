from typing import *

from pydantic import BaseModel, Field

from .cargoes_rules_get_response_supply_check import CargoesRulesGetResponseSupplyCheck


class V1cargoesRulesGetResponse(BaseModel):
    """
    None model
    """

    supply_check_lists: Optional[List[Optional[CargoesRulesGetResponseSupplyCheck]]] = Field(
        alias="supply_check_lists", default=None
    )
