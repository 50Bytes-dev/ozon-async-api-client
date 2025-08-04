from typing import *

from pydantic import BaseModel, Field

from .supply_check_cargoes_present_rule import SupplyCheckCargoesPresentRule
from .supply_check_edit_deadline_expire_rule import SupplyCheckEditDeadlineExpireRule
from .supply_check_expire_date_presented_rule import SupplyCheckExpireDatePresentedRule
from .supply_check_is_valid_distribution_rule import SupplyCheckIsValidDistributionRule
from .supply_check_package_unit_with_distribution_rule import SupplyCheckPackageUnitWithDistributionRule
from .supply_check_placement_zone_rule import SupplyCheckPlacementZoneRule


class CargoesRulesGetResponseSupplyCheck(BaseModel):
    """
    None model

    Чек-лист правил заполнения грузомест.
    """

    cargoes_presents_rule: Optional[SupplyCheckCargoesPresentRule] = Field(alias="cargoes_presents_rule", default=None)

    edit_deadline_expire_rule: Optional[SupplyCheckEditDeadlineExpireRule] = Field(
        alias="edit_deadline_expire_rule", default=None
    )

    expire_dates_presented_rule: Optional[SupplyCheckExpireDatePresentedRule] = Field(
        alias="expire_dates_presented_rule", default=None
    )

    is_valid_distribution_rule: Optional[SupplyCheckIsValidDistributionRule] = Field(
        alias="is_valid_distribution_rule", default=None
    )

    package_units_with_distribution_rule: Optional[SupplyCheckPackageUnitWithDistributionRule] = Field(
        alias="package_units_with_distribution_rule", default=None
    )

    placement_zones_rule: Optional[SupplyCheckPlacementZoneRule] = Field(alias="placement_zones_rule", default=None)

    supply_id: Optional[int] = Field(alias="supply_id", default=None)
