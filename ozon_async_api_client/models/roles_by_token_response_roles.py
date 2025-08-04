from typing import *

from pydantic import BaseModel, Field


class RolesByTokenResponseRoles(BaseModel):
    """
    None model
    """

    name: Optional[str] = Field(alias="name", default=None)

    methods: Optional[List[str]] = Field(alias="methods", default=None)
