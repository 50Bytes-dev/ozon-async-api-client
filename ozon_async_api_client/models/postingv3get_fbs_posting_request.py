from typing import *

from pydantic import BaseModel, Field

from .postingv3fbs_posting_with_params_examplars import Postingv3fbsPostingWithParamsExamplars


class Postingv3getFbsPostingRequest(BaseModel):
    """
    object model
    """

    posting_number: Union[str, int] = Field(alias="posting_number")

    with_: Optional[Postingv3fbsPostingWithParamsExamplars] = Field(alias="with", default=None)
