from typing import *

from pydantic import BaseModel, Field

from .v2posting_fbsact_get_postings_result import V2postingFBSActGetPostingsResult


class V2postingFBSActGetPostingsResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V2postingFBSActGetPostingsResult]]] = Field(alias="result", default=None)
