from typing import *

from pydantic import BaseModel, Field


class OperationPosting(BaseModel):
    """
    object model

    Информация об отправлении.
    """

    delivery_schema: Optional[str] = Field(alias="delivery_schema", default=None)

    order_date: Optional[str] = Field(alias="order_date", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
