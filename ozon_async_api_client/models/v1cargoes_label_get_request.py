from typing import *

from pydantic import BaseModel, Field


class V1cargoesLabelGetRequest(BaseModel):
    """
    None model
    """

    operation_id: Union[str, int] = Field(alias="operation_id")
