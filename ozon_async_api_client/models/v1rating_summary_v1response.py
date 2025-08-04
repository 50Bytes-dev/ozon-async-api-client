from typing import *

from pydantic import BaseModel, Field


class V1ratingSummaryV1response(BaseModel):
    """
    object model
    """

    groups: Optional[Any] = Field(alias="groups", default=None)

    localization_index: Optional[Any] = Field(alias="localization_index", default=None)

    penalty_score_exceeded: Optional[bool] = Field(alias="penalty_score_exceeded", default=None)

    premium: Optional[bool] = Field(alias="premium", default=None)

    premium_plus: Optional[bool] = Field(alias="premium_plus", default=None)
