from typing import *

from pydantic import BaseModel, Field


class CreateReportResponseCode(BaseModel):
    """
    object model

    Результаты запроса.
    """

    code: Optional[Union[str, int]] = Field(alias="code", default=None)
