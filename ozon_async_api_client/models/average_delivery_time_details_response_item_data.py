from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_details_response_item_data_delivery_schema import \
    AverageDeliveryTimeDetailsResponseItemDataDeliverySchema


class AverageDeliveryTimeDetailsResponseItemData(BaseModel):
    """
    None model

    Данные о товаре.
    """

    delivery_schema: Optional[AverageDeliveryTimeDetailsResponseItemDataDeliverySchema] = Field(
        alias="delivery_schema", default=None
    )

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
