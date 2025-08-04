from typing import *

from pydantic import BaseModel, Field

from .v1draft_cluster_list_response_cluster import V1draftClusterListResponseCluster


class V1draftClusterListResponse(BaseModel):
    """
    None model
    """

    clusters: Optional[List[Optional[V1draftClusterListResponseCluster]]] = Field(alias="clusters", default=None)
