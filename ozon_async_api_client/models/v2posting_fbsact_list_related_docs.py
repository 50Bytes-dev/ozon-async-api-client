from typing import *

from pydantic import BaseModel, Field


class V2postingFBSActListRelatedDocs(BaseModel):
    """
    object model

    Информация про акты перевозки.
    """

    act_of_acceptance: Optional[Dict[str, Any]] = Field(alias="act_of_acceptance", default=None)

    act_of_mismatch: Optional[Dict[str, Any]] = Field(alias="act_of_mismatch", default=None)

    act_of_excess: Optional[Dict[str, Any]] = Field(alias="act_of_excess", default=None)
