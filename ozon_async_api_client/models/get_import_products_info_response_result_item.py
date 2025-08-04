from typing import *

from pydantic import BaseModel, Field

from .v1item_error import V1itemError


class GetImportProductsInfoResponseResultItem(BaseModel):
    """
    object model
    """

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    errors: Optional[List[Optional[V1itemError]]] = Field(alias="errors", default=None)
