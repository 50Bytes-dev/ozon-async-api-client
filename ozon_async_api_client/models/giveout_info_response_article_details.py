from typing import *

from pydantic import BaseModel, Field

from .v1giveout_delivery_schema import V1giveoutDeliverySchema


class GiveoutInfoResponseArticleDetails(BaseModel):
    """
    None model
    """

    approved: Optional[bool] = Field(alias="approved", default=None)

    delivery_schema: Optional[V1giveoutDeliverySchema] = Field(alias="delivery_schema", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    seller_id: Optional[int] = Field(alias="seller_id", default=None)
