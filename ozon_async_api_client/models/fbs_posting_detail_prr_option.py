from typing import *

from pydantic import BaseModel, Field


class FbsPostingDetailPrrOption(BaseModel):
    """
    object model

    Информация об услуге погрузочно-разгрузочных работ. Актуально для КГТ-отправлений с доставкой силами продавца или интегрированной службой.
    """

    code: Optional[str] = Field(alias="code", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    floor: Optional[str] = Field(alias="floor", default=None)
