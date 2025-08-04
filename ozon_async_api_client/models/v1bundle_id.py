from typing import *

from pydantic import BaseModel, Field


class V1bundleId(BaseModel):
    """
    None model
    """

    bundle_id: Optional[Union[str, int]] = Field(alias="bundle_id", default=None)

    is_docless: Optional[bool] = Field(alias="is_docless", default=None)
