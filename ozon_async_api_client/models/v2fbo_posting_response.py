from typing import *

from pydantic import BaseModel, Field

from .v2fbo_posting import V2fboPosting


class V2fboPostingResponse(BaseModel):
    """
    object model
    """

    result: Optional[V2fboPosting] = Field(alias="result", default=None)
