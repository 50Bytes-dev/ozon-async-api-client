from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingProductExemplarInfoV3(BaseModel):
    """
    object model
    """

    exemplar_id: Optional[int] = Field(alias="exemplar_id", default=None)

    mandatory_mark: Optional[str] = Field(alias="mandatory_mark", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    is_gtd_absent: Optional[bool] = Field(alias="is_gtd_absent", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)

    is_rnpt_absent: Optional[bool] = Field(alias="is_rnpt_absent", default=None)
