from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoResponseResultItemsQuantInfoQuantsMarketingPrice(BaseModel):
    """
    object model

    Цена на товар с учётом всех акций, которая будет указана на витрине Ozon, без учёта скидки по Ozon Карте.
    """

    price: Optional[str] = Field(alias="price", default=None)

    seller_price: Optional[str] = Field(alias="seller_price", default=None)
