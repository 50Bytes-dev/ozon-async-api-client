from typing import *

from pydantic import BaseModel, Field

from .list_posting_codes_response_posting import ListPostingCodesResponsePosting


class V1listPostingCodesResponse(BaseModel):
    """
    None model
    """

    result: Optional[List[Optional[ListPostingCodesResponsePosting]]] = Field(alias="result", default=None)
