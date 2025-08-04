from typing import *

from pydantic import BaseModel, Field


class GetStrategyListResponseStrategy(BaseModel):
    """
    object model
    """

    id: Optional[Union[str, int]] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    update_type: Optional[str] = Field(alias="update_type", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    products_count: Optional[int] = Field(alias="products_count", default=None)

    competitors_count: Optional[int] = Field(alias="competitors_count", default=None)

    enabled: Optional[bool] = Field(alias="enabled", default=None)
