from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingDetailOptional(BaseModel):
    """
    object model

    Список товаров с дополнительными характеристиками.
    """

    products_with_possible_mandatory_mark: Optional[List[str]] = Field(
        alias="products_with_possible_mandatory_mark", default=None
    )
