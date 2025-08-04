from typing import *

from pydantic import BaseModel, Field

from .v1certificate import V1certificate


class V1productCertificateListResponseResult(BaseModel):
    """
    object model

    Список сертификатов.
    """

    certificates: Optional[List[Optional[V1certificate]]] = Field(alias="certificates", default=None)

    page_count: Optional[int] = Field(alias="page_count", default=None)
