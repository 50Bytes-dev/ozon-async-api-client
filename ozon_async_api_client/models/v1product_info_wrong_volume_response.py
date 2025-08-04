from typing import *

from pydantic import BaseModel, Field


class V1productInfoWrongVolumeResponse(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    products: Optional[Any] = Field(alias="products", default=None)
