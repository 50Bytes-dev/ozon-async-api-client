from typing import *

from pydantic import BaseModel, Field

from .productv4filter import Productv4filter


class Productv4getProductAttributesV4request(BaseModel):
    """
    object model
    """

    filter: Optional[Productv4filter] = Field(alias="filter", default=None)

    last_id: Optional[str] = Field(alias="last_id", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)

    sort_by: Optional[str] = Field(alias="sort_by", default=None)

    sort_dir: Optional[str] = Field(alias="sort_dir", default=None)
