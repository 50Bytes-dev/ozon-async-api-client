from typing import *

from pydantic import BaseModel, Field


class DetailsRfbsDetails(BaseModel):
    """
    object model

    Перечисления по схеме rFBS.
    """

    total: Optional[float] = Field(alias="total", default=None)

    transfer_delivery: Optional[float] = Field(alias="transfer_delivery", default=None)

    transfer_delivery_return: Optional[float] = Field(alias="transfer_delivery_return", default=None)

    compensation_delivery_return: Optional[float] = Field(alias="compensation_delivery_return", default=None)

    partial_compensation: Optional[float] = Field(alias="partial_compensation", default=None)

    partial_compensation_return: Optional[float] = Field(alias="partial_compensation_return", default=None)
