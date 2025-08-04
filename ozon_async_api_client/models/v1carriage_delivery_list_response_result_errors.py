from typing import *

from pydantic import BaseModel, Field


class V1carriageDeliveryListResponseResultErrors(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    status: Optional[str] = Field(alias="status", default=None)
