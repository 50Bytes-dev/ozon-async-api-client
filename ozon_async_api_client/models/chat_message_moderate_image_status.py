from enum import Enum


class ChatMessageModerateImageStatus(str, Enum):

    SUCCESS = "SUCCESS"
    MODERATION = "MODERATION"
    FAILED = "FAILED"
