from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingRequirementsV3(BaseModel):
    """
    object model

    Cписок продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД), регистрационный номер партии товара (РНПТ) или маркировку «Честный ЗНАК», чтобы перевести отправление в следующий статус.
    """

    products_requiring_change_country: Optional[List[str]] = Field(
        alias="products_requiring_change_country", default=None
    )

    products_requiring_gtd: Optional[List[str]] = Field(alias="products_requiring_gtd", default=None)

    products_requiring_country: Optional[List[str]] = Field(alias="products_requiring_country", default=None)

    products_requiring_mandatory_mark: Optional[List[str]] = Field(
        alias="products_requiring_mandatory_mark", default=None
    )

    products_requiring_jw_uin: Optional[List[str]] = Field(alias="products_requiring_jw_uin", default=None)

    products_requiring_rnpt: Optional[List[str]] = Field(alias="products_requiring_rnpt", default=None)
