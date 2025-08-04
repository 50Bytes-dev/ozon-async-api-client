from typing import *

from pydantic import BaseModel, Field


class GetRealizationReportResponseV2header(BaseModel):
    """
    object model

    Титульный лист отчёта.
    """

    contract_date: Optional[str] = Field(alias="contract_date", default=None)

    contract_number: Optional[str] = Field(alias="contract_number", default=None)

    currency_sys_name: Optional[str] = Field(alias="currency_sys_name", default=None)

    doc_amount: Optional[float] = Field(alias="doc_amount", default=None)

    doc_date: Optional[str] = Field(alias="doc_date", default=None)

    number: Optional[str] = Field(alias="number", default=None)

    payer_inn: Optional[str] = Field(alias="payer_inn", default=None)

    payer_kpp: Optional[str] = Field(alias="payer_kpp", default=None)

    payer_name: Optional[str] = Field(alias="payer_name", default=None)

    receiver_inn: Optional[str] = Field(alias="receiver_inn", default=None)

    receiver_kpp: Optional[str] = Field(alias="receiver_kpp", default=None)

    receiver_name: Optional[str] = Field(alias="receiver_name", default=None)

    start_date: Optional[str] = Field(alias="start_date", default=None)

    stop_date: Optional[str] = Field(alias="stop_date", default=None)

    vat_amount: Optional[float] = Field(alias="vat_amount", default=None)
