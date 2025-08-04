from typing import *

from pydantic import BaseModel, Field


class BrandBrandCompanyCertificationListRequest(BaseModel):
    """
    object model
    """

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")
