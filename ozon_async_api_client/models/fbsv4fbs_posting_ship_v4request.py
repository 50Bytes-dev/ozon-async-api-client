from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_ship_v4request_with import FbsPostingShipV4requestWith


class Fbsv4fbsPostingShipV4request(BaseModel):
    """
    object model
    """

    packages: Any = Field(alias="packages")

    posting_number: str = Field(alias="posting_number")

    with_: Optional[FbsPostingShipV4requestWith] = Field(alias="with", default=None)
