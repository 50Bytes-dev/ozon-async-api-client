from typing import *

from pydantic import BaseModel, Field


class V3address(BaseModel):
    """
    object model

    Информация об адресе доставки.
    """

    address_tail: Optional[str] = Field(alias="address_tail", default=None)

    city: Optional[str] = Field(alias="city", default=None)

    comment: Optional[str] = Field(alias="comment", default=None)

    country: Optional[str] = Field(alias="country", default=None)

    district: Optional[str] = Field(alias="district", default=None)

    latitude: Optional[float] = Field(alias="latitude", default=None)

    longitude: Optional[float] = Field(alias="longitude", default=None)

    provider_pvz_code: Optional[str] = Field(alias="provider_pvz_code", default=None)

    pvz_code: Optional[int] = Field(alias="pvz_code", default=None)

    region: Optional[str] = Field(alias="region", default=None)

    zip_code: Optional[str] = Field(alias="zip_code", default=None)
