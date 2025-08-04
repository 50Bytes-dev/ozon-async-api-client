from typing import *

from pydantic import BaseModel, Field


class V2postingFBSGetBarcodeTextResponse(BaseModel):
    """
    object model
    """

    result: Optional[str] = Field(alias="result", default=None)
