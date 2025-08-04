from typing import *

from pydantic import BaseModel, Field

from .value_cargo_type import ValueCargoType
from .value_item import ValueItem


class V1cargoesCreateRequestCargoValue(BaseModel):
    """
    None model

    Информация о грузоместе.
    """

    items: Optional[List[Optional[ValueItem]]] = Field(alias="items", default=None)

    type: ValueCargoType = Field(alias="type")
