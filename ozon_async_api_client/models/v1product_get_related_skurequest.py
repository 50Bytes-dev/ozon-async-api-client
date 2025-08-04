from typing import *

from pydantic import BaseModel, Field


class V1productGetRelatedSKURequest(BaseModel):
    """
    object model
    """

    sku: Any = Field(alias="sku")
