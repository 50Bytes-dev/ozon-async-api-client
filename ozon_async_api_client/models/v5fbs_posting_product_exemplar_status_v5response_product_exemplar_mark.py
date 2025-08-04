from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarStatusV5responseProductExemplarMark(BaseModel):
    """
    None model
    """

    check_status: Optional[str] = Field(alias="check_status", default=None)

    error_codes: Optional[List[str]] = Field(alias="error_codes", default=None)

    mark: Optional[str] = Field(alias="mark", default=None)

    mark_type: Optional[str] = Field(alias="mark_type", default=None)
