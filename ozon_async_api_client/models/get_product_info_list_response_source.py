from typing import *

from pydantic import BaseModel, Field

from .source_shipment_type import SourceShipmentType


class GetProductInfoListResponseSource(BaseModel):
    """
    object model
    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    quant_code: Optional[str] = Field(alias="quant_code", default=None)

    shipment_type: Optional[SourceShipmentType] = Field(alias="shipment_type", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    source: Optional[str] = Field(alias="source", default=None)
