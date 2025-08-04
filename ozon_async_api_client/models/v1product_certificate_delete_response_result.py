from typing import *

from pydantic import BaseModel, Field


class V1productCertificateDeleteResponseResult(BaseModel):
    """
    object model

    Результат удаления сертификата.
    """

    is_delete: Optional[bool] = Field(alias="is_delete", default=None)

    error_message: Optional[str] = Field(alias="error_message", default=None)
