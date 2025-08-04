from typing import *

from pydantic import BaseModel, Field

from .v2fbs_posting import V2fbsPosting


class V2fbsPostingResponse(BaseModel):
    """
    object model

    Информация об отправлении.
    """

    result: Optional[V2fbsPosting] = Field(alias="result", default=None)
