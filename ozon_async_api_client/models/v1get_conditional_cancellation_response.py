from typing import *

from pydantic import BaseModel, Field

from .v1conditional_cancellation import V1conditionalCancellation


class V1getConditionalCancellationResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1conditionalCancellation] = Field(alias="result", default=None)
