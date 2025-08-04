from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsListV2responseState(BaseModel):
    """
    object model

    Статусы заявки и возврата денег.
    """

    group_state: Optional[str] = Field(alias="group_state", default=None)

    money_return_state_name: Optional[str] = Field(alias="money_return_state_name", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    state_name: Optional[str] = Field(alias="state_name", default=None)
