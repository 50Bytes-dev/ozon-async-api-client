from typing import *

from pydantic import BaseModel, Field

from .v3dimensions import V3dimensions


class V3postingProductDetail(BaseModel):
    """
    object model

    Размеры товара.
    """

    dimensions: Optional[V3dimensions] = Field(alias="dimensions", default=None)

    mandatory_mark: Optional[List[str]] = Field(alias="mandatory_mark", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    jw_uin: Optional[List[str]] = Field(alias="jw_uin", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    is_blr_traceable: Optional[bool] = Field(alias="is_blr_traceable", default=None)

    is_marketplace_buyout: Optional[bool] = Field(alias="is_marketplace_buyout", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
