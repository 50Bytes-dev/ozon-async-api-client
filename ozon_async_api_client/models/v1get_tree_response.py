from typing import *

from pydantic import BaseModel, Field

from .v1get_tree_response_item import V1getTreeResponseItem


class V1getTreeResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1getTreeResponseItem]]] = Field(alias="result", default=None)
