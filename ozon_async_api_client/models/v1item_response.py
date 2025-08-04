from typing import *

from pydantic import BaseModel, Field

from .v1bundle_item_shipment_type import V1bundleItemShipmentType
from .v1item_sfbo_attribute import V1itemSfboAttribute


class V1itemResponse(BaseModel):
    """
    object model
    """

    icon_path: Optional[str] = Field(alias="icon_path", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quant: Optional[int] = Field(alias="quant", default=None)

    is_quant_editable: Optional[bool] = Field(alias="is_quant_editable", default=None)

    volume_in_litres: Optional[float] = Field(alias="volume_in_litres", default=None)

    total_volume_in_litres: Optional[float] = Field(alias="total_volume_in_litres", default=None)

    contractor_item_code: Optional[Union[str, int]] = Field(alias="contractor_item_code", default=None)

    sfbo_attribute: Optional[V1itemSfboAttribute] = Field(alias="sfbo_attribute", default=None)

    shipment_type: Optional[V1bundleItemShipmentType] = Field(alias="shipment_type", default=None)

    tags: Optional[List[str]] = Field(alias="tags", default=None)

    placement_zone: Optional[str] = Field(alias="placement_zone", default=None)
