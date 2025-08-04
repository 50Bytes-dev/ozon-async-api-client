from typing import *

from pydantic import BaseModel, Field

from .cargoes_present_rule_cargo_count_per_type_enum import CargoesPresentRuleCargoCountPerTypeEnum


class CargoesPresentRuleCargoCountPerType(BaseModel):
    """
    Количество грузомест каждого типа model
    """

    count: Optional[int] = Field(alias="count", default=None)

    type: Optional[CargoesPresentRuleCargoCountPerTypeEnum] = Field(alias="type", default=None)
