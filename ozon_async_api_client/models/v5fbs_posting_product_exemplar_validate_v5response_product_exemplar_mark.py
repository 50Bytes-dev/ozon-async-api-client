from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarValidateV5responseProductExemplarMark(BaseModel):
    """
    None model
    """

    errors: Optional[List[str]] = Field(alias="errors", default=None)

    mark: Optional[str] = Field(alias="mark", default=None)

    mark_type: Optional[str] = Field(alias="mark_type", default=None)

    valid: Optional[bool] = Field(alias="valid", default=None)
