from typing import *

from pydantic import BaseModel, Field

from .v3import_products_response_result import V3importProductsResponseResult


class V3importProductsResponse(BaseModel):
    """
    None model
    """

    result: Optional[V3importProductsResponseResult] = Field(alias="result", default=None)
