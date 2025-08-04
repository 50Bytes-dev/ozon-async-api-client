from typing import *

from pydantic import BaseModel, Field

from .get_supply_order_bundle_request_item_tags_calculation import GetSupplyOrderBundleRequestItemTagsCalculation
from .v1item_sort_field import V1itemSortField


class V1getSupplyOrderBundleRequest(BaseModel):
    """
    None model
    """

    bundle_ids: List[str] = Field(alias="bundle_ids")

    is_asc: Optional[bool] = Field(alias="is_asc", default=None)

    item_tags_calculation: Optional[GetSupplyOrderBundleRequestItemTagsCalculation] = Field(
        alias="item_tags_calculation", default=None
    )

    last_id: Optional[str] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")

    query: Optional[str] = Field(alias="query", default=None)

    sort_field: Optional[V1itemSortField] = Field(alias="sort_field", default=None)
