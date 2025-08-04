from typing import *

from pydantic import BaseModel, Field


class CreateReportResponseCodeNoDeadline(BaseModel):
    """
    object model

    Результат запроса.
    """

    code: Optional[Union[str, int]] = Field(alias="code", default=None)
