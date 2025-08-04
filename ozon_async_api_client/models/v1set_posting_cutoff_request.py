from typing import *

from pydantic import BaseModel, Field


class V1setPostingCutoffRequest(BaseModel):
    """
    object model
    """

    new_cutoff_date: str = Field(alias="new_cutoff_date")

    posting_number: str = Field(alias="posting_number")
