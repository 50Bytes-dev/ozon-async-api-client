from typing import *

from pydantic import BaseModel, Field

from .v1item_response import V1itemResponse


class V1getSupplyOrderBundleResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V1itemResponse]]] = Field(alias="items", default=None)

    total_count: Optional[int] = Field(alias="total_count", default=None)

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)
