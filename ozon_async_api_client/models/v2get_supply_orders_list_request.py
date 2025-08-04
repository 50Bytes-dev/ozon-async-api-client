from typing import *

from pydantic import BaseModel, Field

from .get_supply_orders_list_request_filter import GetSupplyOrdersListRequestFilter
from .get_supply_orders_list_request_paging import GetSupplyOrdersListRequestPaging


class V2getSupplyOrdersListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[GetSupplyOrdersListRequestFilter] = Field(alias="filter", default=None)

    paging: GetSupplyOrdersListRequestPaging = Field(alias="paging")
