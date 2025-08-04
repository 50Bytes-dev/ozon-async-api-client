from typing import *

from pydantic import BaseModel, Field

from .v1posting_fbs_split_response_posting import V1postingFbsSplitResponsePosting
from .v1posting_fbs_split_response_posting_parent import V1postingFbsSplitResponsePostingParent


class V1postingFbsSplitResponse(BaseModel):
    """
    None model
    """

    parent_posting: Optional[V1postingFbsSplitResponsePostingParent] = Field(alias="parent_posting", default=None)

    postings: Optional[List[Optional[V1postingFbsSplitResponsePosting]]] = Field(alias="postings", default=None)
