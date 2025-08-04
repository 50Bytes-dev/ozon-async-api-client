from typing import *

from pydantic import BaseModel, Field


class PostingFbsPostingSentbysellerResponseItem(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    posting_number: Optional[Union[str, int]] = Field(alias="posting_number", default=None)

    result: Optional[bool] = Field(alias="result", default=None)
