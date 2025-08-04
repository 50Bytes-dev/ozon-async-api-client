from typing import *

from pydantic import BaseModel, Field

from .get_finance_products_buyout_response_product import GetFinanceProductsBuyoutResponseProduct


class V1getFinanceProductsBuyoutResponse(BaseModel):
    """
    None model
    """

    products: Optional[List[Optional[GetFinanceProductsBuyoutResponseProduct]]] = Field(alias="products", default=None)
