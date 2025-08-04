from typing import *

from pydantic import BaseModel, Field

from .draftv1warehouse import Draftv1warehouse


class Draftv1cluster(BaseModel):
    """
    None model
    """

    cluster_id: Optional[int] = Field(alias="cluster_id", default=None)

    cluster_name: Optional[str] = Field(alias="cluster_name", default=None)

    warehouses: Optional[List[Optional[Draftv1warehouse]]] = Field(alias="warehouses", default=None)
