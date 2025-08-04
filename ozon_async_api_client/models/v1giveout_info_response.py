from typing import *

from pydantic import BaseModel, Field

from .giveout_info_response_article_details import GiveoutInfoResponseArticleDetails
from .v1giveout_status import V1giveoutStatus


class V1giveoutInfoResponse(BaseModel):
    """
    None model
    """

    articles: Optional[List[Optional[GiveoutInfoResponseArticleDetails]]] = Field(alias="articles", default=None)

    giveout_id: Optional[int] = Field(alias="giveout_id", default=None)

    giveout_status: Optional[V1giveoutStatus] = Field(alias="giveout_status", default=None)

    warehouse_address: Optional[str] = Field(alias="warehouse_address", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
