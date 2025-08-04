from typing import *

from pydantic import BaseModel, Field


class V1productInfoWrongVolumeRequest(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)
