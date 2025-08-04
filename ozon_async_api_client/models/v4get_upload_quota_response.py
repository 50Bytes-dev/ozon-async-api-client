from typing import *

from pydantic import BaseModel, Field

from .get_upload_quota_response_daily_create import GetUploadQuotaResponseDailyCreate
from .get_upload_quota_response_daily_update import GetUploadQuotaResponseDailyUpdate
from .get_upload_quota_response_total import GetUploadQuotaResponseTotal


class V4getUploadQuotaResponse(BaseModel):
    """
    object model
    """

    daily_create: Optional[GetUploadQuotaResponseDailyCreate] = Field(alias="daily_create", default=None)

    daily_update: Optional[GetUploadQuotaResponseDailyUpdate] = Field(alias="daily_update", default=None)

    total: Optional[GetUploadQuotaResponseTotal] = Field(alias="total", default=None)
