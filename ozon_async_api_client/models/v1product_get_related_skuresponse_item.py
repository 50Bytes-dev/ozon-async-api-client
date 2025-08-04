from typing import *

from pydantic import BaseModel, Field


class V1productGetRelatedSKUResponseItem(BaseModel):
    """
    object model
    """

    availability: Optional[str] = Field(alias="availability", default=None)

    deleted_at: Optional[str] = Field(alias="deleted_at", default=None)

    delivery_schema: Optional[str] = Field(alias="delivery_schema", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
