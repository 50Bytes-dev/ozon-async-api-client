from typing import *

from pydantic import BaseModel, Field


class PostingLegalInfo(BaseModel):
    """
    None model

    Юридическая информация о покупателе.
    """

    company_name: Optional[str] = Field(alias="company_name", default=None)

    inn: Optional[str] = Field(alias="inn", default=None)

    kpp: Optional[str] = Field(alias="kpp", default=None)
