from typing import *

from pydantic import BaseModel, Field


class Productv3getProductListResponseItemQuant(BaseModel):
    """
    object model
    """

    quant_code: Optional[Union[str, int]] = Field(alias="quant_code", default=None)

    quant_size: Optional[int] = Field(alias="quant_size", default=None)
