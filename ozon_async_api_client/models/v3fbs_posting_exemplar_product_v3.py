from typing import *

from pydantic import BaseModel, Field

from .v3fbs_posting_product_exemplar_info_v3 import V3fbsPostingProductExemplarInfoV3


class V3fbsPostingExemplarProductV3(BaseModel):
    """
    object model

    Список товаров и экземпляров.
    """

    exemplars: Optional[List[Optional[V3fbsPostingProductExemplarInfoV3]]] = Field(alias="exemplars", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
