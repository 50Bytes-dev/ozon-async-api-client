from typing import *

from pydantic import BaseModel, Field

from .cargoes_present_rule_cargo_count_per_type import CargoesPresentRuleCargoCountPerType


class SupplyCheckCargoesPresentRule(BaseModel):
    """
    None model

    Правило указания грузомест.
    """

    cargo_count_per_type: Optional[List[Optional[CargoesPresentRuleCargoCountPerType]]] = Field(
        alias="cargo_count_per_type", default=None
    )

    count: Optional[int] = Field(alias="count", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
