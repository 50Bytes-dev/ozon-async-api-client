from typing import *

from pydantic import BaseModel, Field

from .v1competitor import V1competitor


class V1getStrategyResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    competitors: Optional[List[Optional[V1competitor]]] = Field(alias="competitors", default=None)

    enabled: Optional[bool] = Field(alias="enabled", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    update_type: Optional[str] = Field(alias="update_type", default=None)
