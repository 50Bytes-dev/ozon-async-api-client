from typing import *

from pydantic import BaseModel, Field

from .report_language import ReportLanguage


class V1createStockByWarehouseReportRequest(BaseModel):
    """
    object model
    """

    language: Optional[ReportLanguage] = Field(alias="language", default=None)

    warehouseId: Any = Field(alias="warehouseId")
