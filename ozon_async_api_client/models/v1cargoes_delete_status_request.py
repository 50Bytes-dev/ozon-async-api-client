from typing import *

from pydantic import BaseModel, Field


class V1cargoesDeleteStatusRequest(BaseModel):
    """
    None model
    """

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
