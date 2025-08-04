from typing import *

from pydantic import BaseModel, Field


class ReturnsRfbsGetV2responseReturnReason(BaseModel):
    """
    object model

    Данные о причине возврата.
    """

    id: Optional[int] = Field(alias="id", default=None)

    is_defect: Optional[bool] = Field(alias="is_defect", default=None)

    name: Optional[str] = Field(alias="name", default=None)
