from typing import *

from pydantic import BaseModel, Field

from .operation_item import OperationItem
from .operation_posting import OperationPosting
from .operation_service import OperationService


class FinanceTransactionListV3responseOperation(BaseModel):
    """
    object model
    """

    accruals_for_sale: Optional[float] = Field(alias="accruals_for_sale", default=None)

    amount: Optional[float] = Field(alias="amount", default=None)

    delivery_charge: Optional[float] = Field(alias="delivery_charge", default=None)

    items: Optional[List[Optional[OperationItem]]] = Field(alias="items", default=None)

    operation_date: Optional[str] = Field(alias="operation_date", default=None)

    operation_id: Optional[int] = Field(alias="operation_id", default=None)

    operation_type: Optional[str] = Field(alias="operation_type", default=None)

    operation_type_name: Optional[str] = Field(alias="operation_type_name", default=None)

    posting: Optional[OperationPosting] = Field(alias="posting", default=None)

    return_delivery_charge: Optional[float] = Field(alias="return_delivery_charge", default=None)

    sale_commission: Optional[float] = Field(alias="sale_commission", default=None)

    services: Optional[List[Optional[OperationService]]] = Field(alias="services", default=None)

    type: Optional[str] = Field(alias="type", default=None)
