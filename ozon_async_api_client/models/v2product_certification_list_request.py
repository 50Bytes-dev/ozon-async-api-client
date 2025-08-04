from typing import *

from pydantic import BaseModel, Field


class V2productCertificationListRequest(BaseModel):
    """
    None model
    """

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")
