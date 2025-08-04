from typing import *

from pydantic import BaseModel, Field

from .row_item import RowItem
from .row_item_commission import RowItemCommission
from .row_item_commission_return import RowItemCommissionReturn
from .row_item_legal_entity_document import RowItemLegalEntityDocument
from .row_item_order import RowItemOrder


class V1getRealizationReportPostingResponseRow(BaseModel):
    """
    object model
    """

    commission_ratio: Optional[float] = Field(alias="commission_ratio", default=None)

    delivery_commission: Optional[RowItemCommission] = Field(alias="delivery_commission", default=None)

    item: Optional[RowItem] = Field(alias="item", default=None)

    return_commission: Optional[RowItemCommissionReturn] = Field(alias="return_commission", default=None)

    row_number: Optional[int] = Field(alias="row_number", default=None)

    seller_price_per_instance: Optional[float] = Field(alias="seller_price_per_instance", default=None)

    order: Optional[RowItemOrder] = Field(alias="order", default=None)

    legal_entity_document: Optional[RowItemLegalEntityDocument] = Field(alias="legal_entity_document", default=None)
