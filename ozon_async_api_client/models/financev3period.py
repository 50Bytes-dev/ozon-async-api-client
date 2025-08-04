from typing import *

from pydantic import BaseModel, Field


class Financev3period(BaseModel):
    """
    object model

    Период формирования отчёта.
    """

    from_: str = Field(alias="from")

    to: str = Field(alias="to")
