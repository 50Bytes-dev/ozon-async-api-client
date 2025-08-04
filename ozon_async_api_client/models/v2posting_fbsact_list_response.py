from typing import *

from pydantic import BaseModel, Field

from .v2posting_fbsact_list_result import V2postingFBSActListResult


class V2postingFBSActListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V2postingFBSActListResult]]] = Field(alias="result", default=None)
