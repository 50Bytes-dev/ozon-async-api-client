from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_ship_v4request_package_product import FbsPostingShipV4requestPackageProduct


class FbsPostingShipV4requestPackage(BaseModel):
    """
    object model
    """

    products: List[FbsPostingShipV4requestPackageProduct] = Field(alias="products")
