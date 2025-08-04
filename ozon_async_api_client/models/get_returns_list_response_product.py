from typing import *

from pydantic import BaseModel, Field

from .seller_returnsv1money_commission import SellerReturnsv1moneyCommission
from .seller_returnsv1money_product import SellerReturnsv1moneyProduct
from .seller_returnsv1money_without_commission import SellerReturnsv1moneyWithoutCommission


class GetReturnsListResponseProduct(BaseModel):
    """
    object model

    Информация о товаре.
    """

    sku: Optional[int] = Field(alias="sku", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    price: Optional[SellerReturnsv1moneyProduct] = Field(alias="price", default=None)

    price_without_commission: Optional[SellerReturnsv1moneyWithoutCommission] = Field(
        alias="price_without_commission", default=None
    )

    commission_percent: Optional[float] = Field(alias="commission_percent", default=None)

    commission: Optional[SellerReturnsv1moneyCommission] = Field(alias="commission", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)
