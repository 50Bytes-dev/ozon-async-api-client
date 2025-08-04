from typing import *

from pydantic import BaseModel, Field


class ChatMessageContext(BaseModel):
    """
    None model

    Информация о чате.
    """

    order_number: Optional[str] = Field(alias="order_number", default=None)

    sku: Optional[Union[str, int]] = Field(alias="sku", default=None)
