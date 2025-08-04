from typing import *

from pydantic import BaseModel, Field

from .productv4get_product_attributes_v4response_result import Productv4getProductAttributesV4responseResult


class Productv4getProductAttributesV4response(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[Productv4getProductAttributesV4responseResult]]] = Field(
        alias="result", default=None
    )

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

    total: Optional[int] = Field(alias="total", default=None)
