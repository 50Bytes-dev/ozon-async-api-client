from typing import *

from pydantic import BaseModel, Field


class Productv1productInfoPicturesResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    pictures: Optional[Any] = Field(alias="pictures", default=None)
