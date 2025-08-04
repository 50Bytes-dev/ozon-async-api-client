from typing import *

from pydantic import BaseModel, Field

from .v1posting_unpaid_legal_product_list_response_products import V1postingUnpaidLegalProductListResponseProducts


class V1postingUnpaidLegalProductListResponse(BaseModel):
    """
    object model
    """

    products: Optional[List[Optional[V1postingUnpaidLegalProductListResponseProducts]]] = Field(
        alias="products", default=None
    )

    cursor: Optional[str] = Field(alias="cursor", default=None)
