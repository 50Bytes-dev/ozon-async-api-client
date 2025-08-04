from typing import *

from pydantic import BaseModel, Field

from .stocks_import_request_item_stock import StocksImportRequestItemStock


class V1stocksImportRequest(BaseModel):
    """
    None model
    """

    stocks: Optional[List[Optional[StocksImportRequestItemStock]]] = Field(alias="stocks", default=None)
