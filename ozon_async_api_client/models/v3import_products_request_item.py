from typing import *

from pydantic import BaseModel, Field

from .import_product_request_promotion import ImportProductRequestPromotion
from .import_products_request_pdf_list import ImportProductsRequestPdfList
from .v3import_products_request_attribute import V3importProductsRequestAttribute
from .v3import_products_request_complex_attribute import V3importProductsRequestComplexAttribute
from .v3service_type import V3serviceType


class V3importProductsRequestItem(BaseModel):
    """
    object model
    """

    attributes: Optional[List[Optional[V3importProductsRequestAttribute]]] = Field(alias="attributes", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    color_image: Optional[str] = Field(alias="color_image", default=None)

    complex_attributes: Optional[List[Optional[V3importProductsRequestComplexAttribute]]] = Field(
        alias="complex_attributes", default=None
    )

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    depth: Optional[int] = Field(alias="depth", default=None)

    description_category_id: int = Field(alias="description_category_id")

    new_description_category_id: Optional[int] = Field(alias="new_description_category_id", default=None)

    dimension_unit: Optional[str] = Field(alias="dimension_unit", default=None)

    geo_names: Optional[List[str]] = Field(alias="geo_names", default=None)

    height: Optional[int] = Field(alias="height", default=None)

    images: Optional[List[str]] = Field(alias="images", default=None)

    images360: Optional[List[str]] = Field(alias="images360", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    old_price: Optional[str] = Field(alias="old_price", default=None)

    pdf_list: Optional[List[Optional[ImportProductsRequestPdfList]]] = Field(alias="pdf_list", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    primary_image: Optional[str] = Field(alias="primary_image", default=None)

    promotions: Optional[List[Optional[ImportProductRequestPromotion]]] = Field(alias="promotions", default=None)

    service_type: Optional[V3serviceType] = Field(alias="service_type", default=None)

    type_id: int = Field(alias="type_id")

    vat: Optional[str] = Field(alias="vat", default=None)

    weight: Optional[int] = Field(alias="weight", default=None)

    weight_unit: Optional[str] = Field(alias="weight_unit", default=None)

    width: Optional[int] = Field(alias="width", default=None)
