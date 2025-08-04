from typing import *

from pydantic import BaseModel, Field


class V2postingFBSGetBarcodeRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")
