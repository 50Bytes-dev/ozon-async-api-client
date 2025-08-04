from typing import *

from pydantic import BaseModel, Field


class SupplyCheckEditDeadlineExpireRule(BaseModel):
    """
    None model

    Правило крайнего срока редактирования грузомест.
    """

    is_applicable: Optional[bool] = Field(alias="is_applicable", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
