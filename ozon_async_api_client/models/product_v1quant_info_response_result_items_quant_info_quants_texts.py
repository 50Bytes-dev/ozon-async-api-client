from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoResponseResultItemsQuantInfoQuantsTexts(BaseModel):
    """
    object model

    Описание статусов.
    """

    state_description: Optional[str] = Field(alias="state_description", default=None)

    state_name: Optional[str] = Field(alias="state_name", default=None)

    state_sys_name: Optional[str] = Field(alias="state_sys_name", default=None)

    state_tooltip: Optional[str] = Field(alias="state_tooltip", default=None)
