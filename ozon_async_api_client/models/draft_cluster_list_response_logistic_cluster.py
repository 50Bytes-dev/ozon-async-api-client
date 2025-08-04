from typing import *

from pydantic import BaseModel, Field

from .v1draft_cluster_list_response_warehouse import V1draftClusterListResponseWarehouse


class DraftClusterListResponseLogisticCluster(BaseModel):
    """
    None model
    """

    warehouses: Optional[List[Optional[V1draftClusterListResponseWarehouse]]] = Field(alias="warehouses", default=None)
