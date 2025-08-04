from typing import *

from pydantic import BaseModel, Field

from .v4fbs_posting_ship_package_v4request_product import V4fbsPostingShipPackageV4requestProduct


class V4fbsPostingShipPackageV4request(BaseModel):
    """
    None model
    """

    posting_number: str = Field(alias="posting_number")

    products: Optional[List[Optional[V4fbsPostingShipPackageV4requestProduct]]] = Field(alias="products", default=None)
