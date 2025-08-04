from typing import *

from pydantic import BaseModel, Field


class V1getStrategyItemInfoResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    strategy_id: Optional[str] = Field(alias="strategy_id", default=None)

    is_enabled: Optional[bool] = Field(alias="is_enabled", default=None)

    strategy_product_price: Optional[int] = Field(alias="strategy_product_price", default=None)

    price_downloaded_at: Optional[str] = Field(alias="price_downloaded_at", default=None)

    strategy_competitor_id: Optional[int] = Field(alias="strategy_competitor_id", default=None)

    strategy_competitor_product_url: Optional[str] = Field(alias="strategy_competitor_product_url", default=None)
