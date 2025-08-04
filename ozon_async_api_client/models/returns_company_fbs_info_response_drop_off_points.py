from typing import *

from pydantic import BaseModel, Field

from .returns_company_fbs_info_response_pass_info import ReturnsCompanyFbsInfoResponsePassInfo


class ReturnsCompanyFbsInfoResponseDropOffPoints(BaseModel):
    """
    object model
    """

    address: Optional[str] = Field(alias="address", default=None)

    box_count: Optional[int] = Field(alias="box_count", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    pass_info: Optional[ReturnsCompanyFbsInfoResponsePassInfo] = Field(alias="pass_info", default=None)

    place_id: Optional[int] = Field(alias="place_id", default=None)

    returns_count: Optional[int] = Field(alias="returns_count", default=None)

    utc_offset: Optional[str] = Field(alias="utc_offset", default=None)

    warehouses_ids: Optional[List[int]] = Field(alias="warehouses_ids", default=None)
