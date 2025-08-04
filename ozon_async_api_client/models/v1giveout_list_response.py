from typing import *

from pydantic import BaseModel, Field

from .giveout_list_response_giveout_details import GiveoutListResponseGiveoutDetails


class V1giveoutListResponse(BaseModel):
    """
    None model
    """

    giveouts: Optional[List[Optional[GiveoutListResponseGiveoutDetails]]] = Field(alias="giveouts", default=None)
