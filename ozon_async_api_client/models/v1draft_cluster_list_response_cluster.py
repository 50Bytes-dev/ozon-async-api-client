from typing import *

from pydantic import BaseModel, Field

from .draft_cluster_list_response_logistic_cluster import DraftClusterListResponseLogisticCluster


class V1draftClusterListResponseCluster(BaseModel):
    """
    None model
    """

    id: Optional[int] = Field(alias="id", default=None)

    logistic_clusters: Optional[List[Optional[DraftClusterListResponseLogisticCluster]]] = Field(
        alias="logistic_clusters", default=None
    )

    name: Optional[str] = Field(alias="name", default=None)

    type: Optional[str] = Field(alias="type", default=None)
