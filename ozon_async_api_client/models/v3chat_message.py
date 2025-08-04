from typing import *

from pydantic import BaseModel, Field

from .chat_message_context import ChatMessageContext
from .chat_message_moderate_image_status import ChatMessageModerateImageStatus
from .v3user import V3user


class V3chatMessage(BaseModel):
    """
    None model
    """

    context: Optional[ChatMessageContext] = Field(alias="context", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    data: Optional[List[str]] = Field(alias="data", default=None)

    is_image: Optional[bool] = Field(alias="is_image", default=None)

    is_read: Optional[bool] = Field(alias="is_read", default=None)

    message_id: Optional[int] = Field(alias="message_id", default=None)

    moderate_image_status: Optional[ChatMessageModerateImageStatus] = Field(alias="moderate_image_status", default=None)

    user: Optional[V3user] = Field(alias="user", default=None)
