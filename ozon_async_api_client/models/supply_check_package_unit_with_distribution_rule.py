from typing import *

from pydantic import BaseModel, Field


class SupplyCheckPackageUnitWithDistributionRule(BaseModel):
    """
    None model

    Правило заполнения состава грузомест.
    """

    count_all: Optional[int] = Field(alias="count_all", default=None)

    count_with_distribution: Optional[int] = Field(alias="count_with_distribution", default=None)

    is_applicable: Optional[bool] = Field(alias="is_applicable", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
