from typing import *

from pydantic import BaseModel, Field


class CreateDocumentB2bSalesJSONReportResponseBuyer(BaseModel):
    """
    None model

    Информация о покупателе.
    """

    name: Optional[str] = Field(alias="name", default=None)

    address: Optional[str] = Field(alias="address", default=None)

    inn: Optional[str] = Field(alias="inn", default=None)

    kpp: Optional[str] = Field(alias="kpp", default=None)
