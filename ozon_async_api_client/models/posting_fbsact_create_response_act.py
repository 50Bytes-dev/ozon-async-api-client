from typing import *

from pydantic import BaseModel, Field


class PostingFBSActCreateResponseAct(BaseModel):
    """
    object model

    Результат работы метода.
    """

    id: Optional[int] = Field(alias="id", default=None)
