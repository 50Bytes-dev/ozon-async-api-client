from typing import *

from pydantic import BaseModel, Field


class V1analyticsStocksResponseItem(BaseModel):
    """
    object model
    """

    ads: Optional[float] = Field(alias="ads", default=None)

    ads_cluster: Optional[float] = Field(alias="ads_cluster", default=None)

    available_stock_count: Optional[int] = Field(alias="available_stock_count", default=None)

    cluster_id: Optional[int] = Field(alias="cluster_id", default=None)

    cluster_name: Optional[str] = Field(alias="cluster_name", default=None)

    days_without_sales: Optional[int] = Field(alias="days_without_sales", default=None)

    days_without_sales_cluster: Optional[int] = Field(alias="days_without_sales_cluster", default=None)

    excess_stock_count: Optional[int] = Field(alias="excess_stock_count", default=None)

    expiring_stock_count: Optional[int] = Field(alias="expiring_stock_count", default=None)

    idc: Optional[float] = Field(alias="idc", default=None)

    idc_cluster: Optional[float] = Field(alias="idc_cluster", default=None)

    item_tags: Optional[List[str]] = Field(alias="item_tags", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    other_stock_count: Optional[int] = Field(alias="other_stock_count", default=None)

    requested_stock_count: Optional[int] = Field(alias="requested_stock_count", default=None)

    return_from_customer_stock_count: Optional[int] = Field(alias="return_from_customer_stock_count", default=None)

    return_to_seller_stock_count: Optional[int] = Field(alias="return_to_seller_stock_count", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    stock_defect_stock_count: Optional[int] = Field(alias="stock_defect_stock_count", default=None)

    transit_defect_stock_count: Optional[int] = Field(alias="transit_defect_stock_count", default=None)

    transit_stock_count: Optional[int] = Field(alias="transit_stock_count", default=None)

    turnover_grade: Optional[str] = Field(alias="turnover_grade", default=None)

    turnover_grade_cluster: Optional[str] = Field(alias="turnover_grade_cluster", default=None)

    valid_stock_count: Optional[int] = Field(alias="valid_stock_count", default=None)

    waiting_docs_stock_count: Optional[int] = Field(alias="waiting_docs_stock_count", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
