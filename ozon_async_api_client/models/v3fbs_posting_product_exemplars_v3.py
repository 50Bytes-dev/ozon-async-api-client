from typing import *

from pydantic import BaseModel, Field

from .v3fbs_posting_exemplar_product_v3 import V3fbsPostingExemplarProductV3


class V3fbsPostingProductExemplarsV3(BaseModel):
    """
        object model

        Информация по продуктам и их экзмеплярам.

    Ответ содержит поле `product_exemplars`, если в запросе передан признак `with.product_exemplars = true`.

    """

    products: Optional[List[Optional[V3fbsPostingExemplarProductV3]]] = Field(alias="products", default=None)
