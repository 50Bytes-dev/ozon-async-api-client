from typing import *

from pydantic import BaseModel, Field


class Fbsv4getProductExemplarStatusResponseProductExemplar(BaseModel):
    """
    object model
    """

    exemplar_id: Optional[int] = Field(alias="exemplar_id", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    gtd_check_status: Optional[str] = Field(alias="gtd_check_status", default=None)

    gtd_error_codes: Optional[Any] = Field(alias="gtd_error_codes", default=None)

    is_gtd_absent: Optional[bool] = Field(alias="is_gtd_absent", default=None)

    jw_uin: Optional[List[str]] = Field(alias="jw_uin", default=None)

    jw_uin_check_status: Optional[str] = Field(alias="jw_uin_check_status", default=None)

    jw_uin_error_codes: Optional[List[str]] = Field(alias="jw_uin_error_codes", default=None)

    mandatory_mark: Optional[str] = Field(alias="mandatory_mark", default=None)

    mandatory_mark_check_status: Optional[str] = Field(alias="mandatory_mark_check_status", default=None)

    mandatory_mark_error_codes: Optional[Any] = Field(alias="mandatory_mark_error_codes", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)

    rnpt_check_status: Optional[str] = Field(alias="rnpt_check_status", default=None)

    rnpt_error_codes: Optional[Any] = Field(alias="rnpt_error_codes", default=None)

    is_rnpt_absent: Optional[bool] = Field(alias="is_rnpt_absent", default=None)
