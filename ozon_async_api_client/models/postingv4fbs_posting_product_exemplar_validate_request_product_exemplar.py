from typing import *

from pydantic import BaseModel, Field


class Postingv4fbsPostingProductExemplarValidateRequestProductExemplar(BaseModel):
    """
    object model
    """

    gtd: Optional[str] = Field(alias="gtd", default=None)

    mandatory_mark: str = Field(alias="mandatory_mark")

    jw_uin: Optional[List[str]] = Field(alias="jw_uin", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)
