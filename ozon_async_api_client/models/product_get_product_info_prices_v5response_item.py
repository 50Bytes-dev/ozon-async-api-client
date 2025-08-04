from typing import *

from pydantic import BaseModel, Field

from .get_product_info_prices_response_item_price_indexes import GetProductInfoPricesResponseItemPriceIndexes
from .item_commissionsv5 import ItemCommissionsv5
from .item_marketing import ItemMarketing
from .item_pricev5 import ItemPricev5


class ProductGetProductInfoPricesV5responseItem(BaseModel):
    """
    object model
    """

    acquiring: Optional[int] = Field(alias="acquiring", default=None)

    commissions: Optional[ItemCommissionsv5] = Field(alias="commissions", default=None)

    marketing_actions: Optional[ItemMarketing] = Field(alias="marketing_actions", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    price: Optional[ItemPricev5] = Field(alias="price", default=None)

    price_indexes: Optional[GetProductInfoPricesResponseItemPriceIndexes] = Field(alias="price_indexes", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    volume_weight: Optional[float] = Field(alias="volume_weight", default=None)
