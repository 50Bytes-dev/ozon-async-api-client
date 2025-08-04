from typing import *

from pydantic import BaseModel, Field

from .v1giveout_status import V1giveoutStatus


class GiveoutListResponseGiveoutDetails(BaseModel):
    """
    None model
    """

    approved_articles_count: Optional[int] = Field(alias="approved_articles_count", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    giveout_id: Optional[int] = Field(alias="giveout_id", default=None)

    giveout_status: Optional[V1giveoutStatus] = Field(alias="giveout_status", default=None)

    total_articles_count: Optional[int] = Field(alias="total_articles_count", default=None)

    warehouse_address: Optional[str] = Field(alias="warehouse_address", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
