from typing import *

from pydantic import BaseModel, Field


class CreateReportResponseCode(BaseModel):
    """
    object model

    Результаты запроса.
    """

    code: Optional[str] = Field(alias="code", default=None)
