from typing import *

from pydantic import BaseModel, Field


class ProductUpdateOfferIdRequestUpdateOfferId(BaseModel):
    """
    object model
    """

    new_offer_id: str = Field(alias="new_offer_id")

    offer_id: str = Field(alias="offer_id")
