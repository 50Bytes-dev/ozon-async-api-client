from typing import *

from pydantic import BaseModel, Field


class V1analyticsStocksRequest(BaseModel):
    """
    object model
    """

    cluster_ids: Optional[List[str]] = Field(alias="cluster_ids", default=None)

    item_tags: Optional[List[str]] = Field(alias="item_tags", default=None)

    skus: List[str] = Field(alias="skus")

    turnover_grades: Optional[List[str]] = Field(alias="turnover_grades", default=None)

    warehouse_ids: Optional[List[str]] = Field(alias="warehouse_ids", default=None)
