from typing import *

from pydantic import BaseModel, Field


class CreateReportResponseCodeNoDeadline(BaseModel):
    """
    object model

    Результат запроса.
    """

    code: Optional[str] = Field(alias="code", default=None)
