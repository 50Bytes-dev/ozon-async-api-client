from typing import *

from pydantic import BaseModel, Field

from .get_seller_actions_v1response_action import GetSellerActionsV1responseAction


class SellerApiGetSellerActionsV1response(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[GetSellerActionsV1responseAction]]] = Field(alias="result", default=None)
