from typing import *

from pydantic import BaseModel, Field

from .v1get_attributes_response_attribute import V1getAttributesResponseAttribute


class V1getAttributesResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1getAttributesResponseAttribute]]] = Field(alias="result", default=None)
