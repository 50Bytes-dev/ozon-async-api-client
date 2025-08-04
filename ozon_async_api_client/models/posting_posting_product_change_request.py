from typing import *

from pydantic import BaseModel, Field

from .posting_product_change_request_item import PostingProductChangeRequestItem


class PostingPostingProductChangeRequest(BaseModel):
    """
    object model
    """

    items: List[PostingProductChangeRequestItem] = Field(alias="items")

    posting_number: Union[str, int] = Field(alias="posting_number")
