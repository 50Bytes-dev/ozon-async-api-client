from typing import *

from pydantic import BaseModel, Field


class FbsPostingDetailCourier(BaseModel):
    """
    object model

    Данные о курьере.
    """

    car_model: Optional[str] = Field(alias="car_model", default=None)

    car_number: Optional[str] = Field(alias="car_number", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    phone: Optional[str] = Field(alias="phone", default=None)
