from typing import *

from pydantic import BaseModel, Field

from .v1product_fbs_split import V1productFbsSplit


class V1postingFbsSplitRequestPosting(BaseModel):
    """
    None model
    """

    products: List[V1productFbsSplit] = Field(alias="products")
