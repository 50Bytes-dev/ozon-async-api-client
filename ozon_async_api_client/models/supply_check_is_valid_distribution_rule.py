from typing import *

from pydantic import BaseModel, Field


class SupplyCheckIsValidDistributionRule(BaseModel):
    """
    None model

    Правило совпадения составов грузомест с составом поставки.
    """

    count_distributed_sku: Optional[int] = Field(alias="count_distributed_sku", default=None)

    count_sku_total: Optional[int] = Field(alias="count_sku_total", default=None)

    is_applicable: Optional[bool] = Field(alias="is_applicable", default=None)

    percents_int: Optional[int] = Field(alias="percents_int", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
