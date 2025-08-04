from typing import *

from pydantic import BaseModel, Field


class V3deliveryMethod(BaseModel):
    """
    object model

    Метод доставки.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    tpl_provider: Optional[str] = Field(alias="tpl_provider", default=None)

    tpl_provider_id: Optional[int] = Field(alias="tpl_provider_id", default=None)

    warehouse: Optional[str] = Field(alias="warehouse", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
