from typing import *

from pydantic import BaseModel, Field


class V1cargoesLabelGetResponseResult(BaseModel):
    """
    None model

    Информация об этикетках.
    """

    file_guid: Optional[str] = Field(alias="file_guid", default=None)
