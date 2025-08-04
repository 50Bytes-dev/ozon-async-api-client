from typing import *

from pydantic import BaseModel, Field

from .v2posting_fbsact_get_products import V2postingFBSActGetProducts


class V2postingFBSActGetPostingsResult(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    seller_error: Optional[str] = Field(alias="seller_error", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    products: Optional[List[Optional[V2postingFBSActGetProducts]]] = Field(alias="products", default=None)
