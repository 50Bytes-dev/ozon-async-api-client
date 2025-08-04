from typing import *

from pydantic import BaseModel, Field

from .posting_financial_data_product import PostingFinancialDataProduct


class V2postingFinancialData(BaseModel):
    """
    object model

    Финансовые данные.
    """

    cluster_from: Optional[str] = Field(alias="cluster_from", default=None)

    cluster_to: Optional[str] = Field(alias="cluster_to", default=None)

    products: Optional[List[Optional[PostingFinancialDataProduct]]] = Field(alias="products", default=None)
