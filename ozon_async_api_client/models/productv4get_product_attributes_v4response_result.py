from typing import *

from pydantic import BaseModel, Field

from .get_product_attributes_response_image import GetProductAttributesResponseImage
from .get_product_attributes_v4response_attribute import GetProductAttributesV4responseAttribute
from .product_get_product_attributes_v4response_attribute import ProductGetProductAttributesV4responseAttribute
from .v4get_product_attributes_response_model_info import V4getProductAttributesResponseModelInfo
from .v4get_product_attributes_response_pdf import V4getProductAttributesResponsePdf


class Productv4getProductAttributesV4responseResult(BaseModel):
    """
    object model
    """

    attributes: Optional[List[Optional[ProductGetProductAttributesV4responseAttribute]]] = Field(
        alias="attributes", default=None
    )

    attributes_with_defaults: Optional[List[int]] = Field(alias="attributes_with_defaults", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    barcodes: Optional[List[str]] = Field(alias="barcodes", default=None)

    description_category_id: Optional[int] = Field(alias="description_category_id", default=None)

    color_image: Optional[str] = Field(alias="color_image", default=None)

    complex_attributes: Optional[List[Optional[GetProductAttributesV4responseAttribute]]] = Field(
        alias="complex_attributes", default=None
    )

    depth: Optional[int] = Field(alias="depth", default=None)

    dimension_unit: Optional[str] = Field(alias="dimension_unit", default=None)

    height: Optional[int] = Field(alias="height", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    images: Optional[List[Optional[GetProductAttributesResponseImage]]] = Field(alias="images", default=None)

    model_info: Optional[V4getProductAttributesResponseModelInfo] = Field(alias="model_info", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    pdf_list: Optional[List[Optional[V4getProductAttributesResponsePdf]]] = Field(alias="pdf_list", default=None)

    primary_image: Optional[str] = Field(alias="primary_image", default=None)

    sku: Optional[str] = Field(alias="sku", default=None)

    type_id: Optional[int] = Field(alias="type_id", default=None)

    weight: Optional[int] = Field(alias="weight", default=None)

    weight_unit: Optional[str] = Field(alias="weight_unit", default=None)

    width: Optional[int] = Field(alias="width", default=None)
