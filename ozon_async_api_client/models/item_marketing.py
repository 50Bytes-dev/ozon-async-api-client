from typing import *

from pydantic import BaseModel, Field

from .marketing_action import MarketingAction


class ItemMarketing(BaseModel):
    """
    object model

    Маркетинговые акции продавца.
    """

    actions: Optional[List[Optional[MarketingAction]]] = Field(alias="actions", default=None)

    current_period_from: Optional[str] = Field(alias="current_period_from", default=None)

    current_period_to: Optional[str] = Field(alias="current_period_to", default=None)

    ozon_actions_exist: Optional[bool] = Field(alias="ozon_actions_exist", default=None)
