from typing import *

from pydantic import BaseModel, Field


class V2invoiceCreateOrUpdateV2response(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)
