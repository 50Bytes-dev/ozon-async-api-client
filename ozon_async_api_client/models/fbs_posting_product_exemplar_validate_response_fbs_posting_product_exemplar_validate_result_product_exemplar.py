from typing import *

from pydantic import BaseModel, Field


class FbsPostingProductExemplarValidateResponseFbsPostingProductExemplarValidateResultProductExemplar(BaseModel):
    """
    object model
    """

    errors: Optional[Any] = Field(alias="errors", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    mandatory_mark: Optional[str] = Field(alias="mandatory_mark", default=None)

    jw_uin: Optional[List[str]] = Field(alias="jw_uin", default=None)

    valid: Optional[bool] = Field(alias="valid", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)
