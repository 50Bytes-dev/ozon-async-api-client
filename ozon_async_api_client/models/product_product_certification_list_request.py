from typing import *

from pydantic import BaseModel, Field


class ProductProductCertificationListRequest(BaseModel):
    """
    object model
    """

    page: Optional[int] = Field(alias="page", default=None)

    page_size: Optional[int] = Field(alias="page_size", default=None)
