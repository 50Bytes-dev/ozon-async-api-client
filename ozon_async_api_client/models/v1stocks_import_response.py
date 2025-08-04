from typing import *

from pydantic import BaseModel, Field

from .stocks_import_response_item_status import StocksImportResponseItemStatus


class V1stocksImportResponse(BaseModel):
    """
    None model
    """

    status: Optional[List[Optional[StocksImportResponseItemStatus]]] = Field(alias="status", default=None)
