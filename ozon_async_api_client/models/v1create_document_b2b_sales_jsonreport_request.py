from typing import *

from pydantic import BaseModel, Field


class V1createDocumentB2bSalesJSONReportRequest(BaseModel):
    """
    None model
    """

    date: Optional[str] = Field(alias="date", default=None)
