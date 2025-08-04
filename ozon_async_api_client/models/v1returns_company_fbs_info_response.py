from typing import *

from pydantic import BaseModel, Field

from .returns_company_fbs_info_response_drop_off_points import ReturnsCompanyFbsInfoResponseDropOffPoints


class V1returnsCompanyFbsInfoResponse(BaseModel):
    """
    object model
    """

    drop_off_points: Optional[List[Optional[ReturnsCompanyFbsInfoResponseDropOffPoints]]] = Field(
        alias="drop_off_points", default=None
    )

    has_next: Optional[bool] = Field(alias="has_next", default=None)
