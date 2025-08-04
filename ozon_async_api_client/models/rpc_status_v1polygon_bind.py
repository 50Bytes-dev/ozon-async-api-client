from typing import *

from pydantic import BaseModel, Field

from .protobuf_any import ProtobufAny


class RpcStatusV1polygonBind(BaseModel):
    """
    object model
    """

    code: Optional[int] = Field(alias="code", default=None)

    details: Optional[List[Optional[ProtobufAny]]] = Field(alias="details", default=None)

    message: Optional[str] = Field(alias="message", default=None)
