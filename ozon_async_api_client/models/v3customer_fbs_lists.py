from typing import *

from pydantic import BaseModel, Field

from .v3address import V3address


class V3customerFbsLists(BaseModel):
    """
    object model

    Данные о покупателе.
    """

    address: Optional[V3address] = Field(alias="address", default=None)

    customer_id: Optional[int] = Field(alias="customer_id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    phone: Optional[str] = Field(alias="phone", default=None)
