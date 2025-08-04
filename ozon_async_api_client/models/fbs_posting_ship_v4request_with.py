from typing import *

from pydantic import BaseModel, Field


class FbsPostingShipV4requestWith(BaseModel):
    """
    object model

    Дополнительная информация.
    """

    additional_data: Optional[bool] = Field(alias="additional_data", default=None)
