from typing import *

from pydantic import BaseModel, Field


class GetReturnsListResponseLogistic(BaseModel):
    """
    object model

    Информация о возврате.
    """

    technical_return_moment: Optional[str] = Field(alias="technical_return_moment", default=None)

    final_moment: Optional[str] = Field(alias="final_moment", default=None)

    cancelled_with_compensation_moment: Optional[str] = Field(alias="cancelled_with_compensation_moment", default=None)

    return_date: Optional[str] = Field(alias="return_date", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)
