from typing import *

from pydantic import BaseModel, Field

from .delete_products_response_delete_status import DeleteProductsResponseDeleteStatus


class Productv2deleteProductsResponse(BaseModel):
    """
    object model
    """

    status: Optional[List[Optional[DeleteProductsResponseDeleteStatus]]] = Field(alias="status", default=None)
