from typing import *

from pydantic import BaseModel, Field


class ReportCreateCompanyPostingsReportRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    cancel_reason_id: Optional[List[int]] = Field(alias="cancel_reason_id", default=None)

    delivery_schema: Optional[List[str]] = Field(alias="delivery_schema", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    processed_at_from: Optional[str] = Field(alias="processed_at_from", default=None)

    processed_at_to: Optional[str] = Field(alias="processed_at_to", default=None)

    sku: Optional[List[int]] = Field(alias="sku", default=None)

    status_alias: Optional[List[str]] = Field(alias="status_alias", default=None)

    statuses: Optional[List[int]] = Field(alias="statuses", default=None)

    title: Optional[str] = Field(alias="title", default=None)
