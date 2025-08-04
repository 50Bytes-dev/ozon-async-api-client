from typing import *

from pydantic import BaseModel, Field

from .v1posting_fbs_split_request_posting import V1postingFbsSplitRequestPosting


class V1postingFbsSplitRequest(BaseModel):
    """
    None model
    """

    posting_number: str = Field(alias="posting_number")

    postings: List[V1postingFbsSplitRequestPosting] = Field(alias="postings")
