from typing import *

from pydantic import BaseModel, Field


class GetProductInfoListResponseStatuses(BaseModel):
    """
    object model

    Информация о статусах товара.
    """

    is_created: Optional[bool] = Field(alias="is_created", default=None)

    moderate_status: Optional[str] = Field(alias="moderate_status", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    status_description: Optional[str] = Field(alias="status_description", default=None)

    status_failed: Optional[str] = Field(alias="status_failed", default=None)

    status_name: Optional[str] = Field(alias="status_name", default=None)

    status_tooltip: Optional[str] = Field(alias="status_tooltip", default=None)

    status_updated_at: Optional[str] = Field(alias="status_updated_at", default=None)

    validation_status: Optional[str] = Field(alias="validation_status", default=None)
