from typing import *

from pydantic import BaseModel, Field

from .roles_by_token_response_roles import RolesByTokenResponseRoles


class V1rolesByTokenResponse(BaseModel):
    """
    None model
    """

    roles: Optional[List[Optional[RolesByTokenResponseRoles]]] = Field(alias="roles", default=None)
