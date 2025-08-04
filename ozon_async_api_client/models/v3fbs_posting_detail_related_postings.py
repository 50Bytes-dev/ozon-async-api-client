from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingDetailRelatedPostings(BaseModel):
    """
    object model

    Связанные отправления.
    """

    related_posting_numbers: Optional[Any] = Field(alias="related_posting_numbers", default=None)
