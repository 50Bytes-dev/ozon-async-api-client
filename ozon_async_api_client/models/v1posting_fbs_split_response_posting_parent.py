from typing import *

from pydantic import BaseModel, Field

from .v1product_fbs_split import V1productFbsSplit


class V1postingFbsSplitResponsePostingParent(BaseModel):
    """
    None model

    Информация об изначальном отправлении.
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V1productFbsSplit]]] = Field(alias="products", default=None)
