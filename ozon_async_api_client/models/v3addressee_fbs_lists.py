from typing import *

from pydantic import BaseModel, Field


class V3addresseeFbsLists(BaseModel):
    """
    object model

    Контактные данные получателя.
    """

    name: Optional[str] = Field(alias="name", default=None)

    phone: Optional[str] = Field(alias="phone", default=None)
