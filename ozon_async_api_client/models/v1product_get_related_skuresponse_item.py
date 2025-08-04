from typing import *

from pydantic import BaseModel, Field


class V1productGetRelatedSKUResponseItem(BaseModel):
    """
    object model
    """

    availability: Optional[Union[str, int]] = Field(alias="availability", default=None)

    deleted_at: Optional[str] = Field(alias="deleted_at", default=None)

    delivery_schema: Optional[Union[str, int]] = Field(alias="delivery_schema", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
