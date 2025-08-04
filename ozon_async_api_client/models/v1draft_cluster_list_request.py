from typing import *

from pydantic import BaseModel, Field

from .v1cluster_type import V1clusterType


class V1draftClusterListRequest(BaseModel):
    """
    None model
    """

    cluster_ids: Optional[List[int]] = Field(alias="cluster_ids", default=None)

    cluster_type: V1clusterType = Field(alias="cluster_type")
