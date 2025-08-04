from typing import *

from pydantic import BaseModel, Field

from .get_etgb_response_result_etgb import GetEtgbResponseResultEtgb


class GetEtgbResponseResult(BaseModel):
    """
    object model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    etgb: Optional[GetEtgbResponseResultEtgb] = Field(alias="etgb", default=None)
