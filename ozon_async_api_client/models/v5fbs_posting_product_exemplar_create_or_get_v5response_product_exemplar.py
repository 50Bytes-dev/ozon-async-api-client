from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarCreateOrGetV5responseProductExemplar(BaseModel):
    """
    None model
    """

    exemplar_id: Optional[int] = Field(alias="exemplar_id", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    is_gtd_absent: Optional[bool] = Field(alias="is_gtd_absent", default=None)

    is_rnpt_absent: Optional[bool] = Field(alias="is_rnpt_absent", default=None)

    mandatory_mark: Optional[str] = Field(alias="mandatory_mark", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)

    jw_uin: Optional[str] = Field(alias="jw_uin", default=None)
