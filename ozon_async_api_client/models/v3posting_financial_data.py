from typing import *

from pydantic import BaseModel, Field

from .posting_financial_data_product import PostingFinancialDataProduct


class V3postingFinancialData(BaseModel):
    """
    object model

    Данные о стоимости товара, размере скидки, выплате и комиссии.
    """

    cluster_from: Optional[str] = Field(alias="cluster_from", default=None)

    cluster_to: Optional[str] = Field(alias="cluster_to", default=None)

    products: Optional[List[Optional[PostingFinancialDataProduct]]] = Field(alias="products", default=None)
