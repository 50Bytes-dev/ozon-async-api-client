from typing import *

from pydantic import BaseModel, Field


class V3fbsTariffication(BaseModel):
    """
    None model
    """

    current_tariff_rate: Optional[float] = Field(alias="current_tariff_rate", default=None)

    current_tariff_type: Optional[str] = Field(alias="current_tariff_type", default=None)

    current_tariff_charge: Optional[str] = Field(alias="current_tariff_charge", default=None)

    current_tariff_charge_currency_code: Optional[str] = Field(
        alias="current_tariff_charge_currency_code", default=None
    )

    next_tariff_rate: Optional[float] = Field(alias="next_tariff_rate", default=None)

    next_tariff_type: Optional[str] = Field(alias="next_tariff_type", default=None)

    next_tariff_charge: Optional[str] = Field(alias="next_tariff_charge", default=None)

    next_tariff_starts_at: Optional[str] = Field(alias="next_tariff_starts_at", default=None)

    next_tariff_charge_currency_code: Optional[str] = Field(alias="next_tariff_charge_currency_code", default=None)
