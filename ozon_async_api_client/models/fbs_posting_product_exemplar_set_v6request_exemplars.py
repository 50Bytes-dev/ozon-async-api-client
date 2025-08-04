from typing import *

from pydantic import BaseModel, Field

from .exemplars_marks import ExemplarsMarks


class FbsPostingProductExemplarSetV6requestExemplars(BaseModel):
    """
    None model
    """

    exemplar_id: Optional[int] = Field(alias="exemplar_id", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    is_gtd_absent: Optional[bool] = Field(alias="is_gtd_absent", default=None)

    is_rnpt_absent: Optional[bool] = Field(alias="is_rnpt_absent", default=None)

    marks: Optional[List[Optional[ExemplarsMarks]]] = Field(alias="marks", default=None)

    rnpt: Optional[str] = Field(alias="rnpt", default=None)
