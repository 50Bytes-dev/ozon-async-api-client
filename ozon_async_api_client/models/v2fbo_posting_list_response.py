from typing import *

from pydantic import BaseModel, Field

from .v2fbo_posting import V2fboPosting


class V2fboPostingListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V2fboPosting]]] = Field(alias="result", default=None)
