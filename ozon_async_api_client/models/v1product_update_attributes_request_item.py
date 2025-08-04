from typing import *

from pydantic import BaseModel, Field


class V1productUpdateAttributesRequestItem(BaseModel):
    """
    object model
    """

    attributes: Optional[Any] = Field(alias="attributes", default=None)

    offer_id: Union[str, int] = Field(alias="offer_id")
