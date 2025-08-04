from typing import *

from pydantic import BaseModel, Field

from .returns_company_fbs_info_request_pagination import ReturnsCompanyFbsInfoRequestPagination
from .v1returns_company_fbs_info_request_filter import V1returnsCompanyFbsInfoRequestFilter


class V1returnsCompanyFbsInfoRequest(BaseModel):
    """
    object model
    """

    filter: Optional[V1returnsCompanyFbsInfoRequestFilter] = Field(alias="filter", default=None)

    pagination: ReturnsCompanyFbsInfoRequestPagination = Field(alias="pagination")
