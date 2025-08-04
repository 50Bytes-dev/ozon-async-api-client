from typing import *

from pydantic import BaseModel, Field


class SupplyCheckPlacementZoneRule(BaseModel):
    """
    None model

    Правило распределения товаров в грузоместах по зонам размещения.
    """

    count_cargoes_all: Optional[int] = Field(alias="count_cargoes_all", default=None)

    count_cargoes_with_mono_placement_zone: Optional[int] = Field(
        alias="count_cargoes_with_mono_placement_zone", default=None
    )

    is_applicable: Optional[bool] = Field(alias="is_applicable", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
