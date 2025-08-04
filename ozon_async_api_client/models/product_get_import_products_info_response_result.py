from typing import *

from pydantic import BaseModel, Field

from .get_import_products_info_response_result_item import GetImportProductsInfoResponseResultItem


class ProductGetImportProductsInfoResponseResult(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[GetImportProductsInfoResponseResultItem]]] = Field(alias="items", default=None)

    total: Optional[int] = Field(alias="total", default=None)
