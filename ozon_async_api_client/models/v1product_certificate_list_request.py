from typing import *

from pydantic import BaseModel, Field


class V1productCertificateListRequest(BaseModel):
    """
    object model
    """

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")
