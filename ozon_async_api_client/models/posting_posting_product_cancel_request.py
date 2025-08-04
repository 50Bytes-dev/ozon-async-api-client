from typing import *

from pydantic import BaseModel, Field

from .posting_product_cancel_request_item import PostingProductCancelRequestItem


class PostingPostingProductCancelRequest(BaseModel):
    """
    object model
    """

    cancel_reason_id: int = Field(alias="cancel_reason_id")

    cancel_reason_message: str = Field(alias="cancel_reason_message")

    items: List[PostingProductCancelRequestItem] = Field(alias="items")

    posting_number: Union[str, int] = Field(alias="posting_number")
