from typing import *

from pydantic import BaseModel, Field

from .product_v1quant_info_response_result_items_quant_info_quants_dimensions import \
    ProductV1quantInfoResponseResultItemsQuantInfoQuantsDimensions
from .product_v1quant_info_response_result_items_quant_info_quants_marketing_price import \
    ProductV1quantInfoResponseResultItemsQuantInfoQuantsMarketingPrice
from .product_v1quant_info_response_result_items_quant_info_quants_texts import \
    ProductV1quantInfoResponseResultItemsQuantInfoQuantsTexts


class ProductV1quantInfoResponseResultItemsQuantInfoQuants(BaseModel):
    """
    object model
    """

    barcodes_extended: Optional[Any] = Field(alias="barcodes_extended", default=None)

    dimensions: Optional[ProductV1quantInfoResponseResultItemsQuantInfoQuantsDimensions] = Field(
        alias="dimensions", default=None
    )

    marketing_price: Optional[ProductV1quantInfoResponseResultItemsQuantInfoQuantsMarketingPrice] = Field(
        alias="marketing_price", default=None
    )

    min_price: Optional[str] = Field(alias="min_price", default=None)

    old_price: Optional[str] = Field(alias="old_price", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    quant_code: Optional[str] = Field(alias="quant_code", default=None)

    quant_sice: Optional[int] = Field(alias="quant_sice", default=None)

    shipment_type: Optional[str] = Field(alias="shipment_type", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    statuses: Optional[ProductV1quantInfoResponseResultItemsQuantInfoQuantsTexts] = Field(
        alias="statuses", default=None
    )
