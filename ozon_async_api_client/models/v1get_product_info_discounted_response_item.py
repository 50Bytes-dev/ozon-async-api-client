from typing import *

from pydantic import BaseModel, Field


class V1getProductInfoDiscountedResponseItem(BaseModel):
    """
    object model
    """

    comment_reason_damaged: Optional[str] = Field(alias="comment_reason_damaged", default=None)

    condition: Optional[str] = Field(alias="condition", default=None)

    condition_estimation: Optional[str] = Field(alias="condition_estimation", default=None)

    defects: Optional[str] = Field(alias="defects", default=None)

    discounted_sku: Optional[int] = Field(alias="discounted_sku", default=None)

    mechanical_damage: Optional[str] = Field(alias="mechanical_damage", default=None)

    package_damage: Optional[str] = Field(alias="package_damage", default=None)

    packaging_violation: Optional[str] = Field(alias="packaging_violation", default=None)

    reason_damaged: Optional[str] = Field(alias="reason_damaged", default=None)

    repair: Optional[str] = Field(alias="repair", default=None)

    shortage: Optional[str] = Field(alias="shortage", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    warranty_type: Optional[str] = Field(alias="warranty_type", default=None)
