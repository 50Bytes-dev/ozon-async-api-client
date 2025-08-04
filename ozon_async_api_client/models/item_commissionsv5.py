from typing import *

from pydantic import BaseModel, Field


class ItemCommissionsv5(BaseModel):
    """
    object model

    Информация о комиссиях.
    """

    fbo_deliv_to_customer_amount: Optional[float] = Field(alias="fbo_deliv_to_customer_amount", default=None)

    fbo_direct_flow_trans_max_amount: Optional[float] = Field(alias="fbo_direct_flow_trans_max_amount", default=None)

    fbo_direct_flow_trans_min_amount: Optional[float] = Field(alias="fbo_direct_flow_trans_min_amount", default=None)

    fbo_return_flow_amount: Optional[float] = Field(alias="fbo_return_flow_amount", default=None)

    fbs_deliv_to_customer_amount: Optional[float] = Field(alias="fbs_deliv_to_customer_amount", default=None)

    fbs_direct_flow_trans_max_amount: Optional[float] = Field(alias="fbs_direct_flow_trans_max_amount", default=None)

    fbs_direct_flow_trans_min_amount: Optional[float] = Field(alias="fbs_direct_flow_trans_min_amount", default=None)

    fbs_first_mile_max_amount: Optional[float] = Field(alias="fbs_first_mile_max_amount", default=None)

    fbs_first_mile_min_amount: Optional[float] = Field(alias="fbs_first_mile_min_amount", default=None)

    fbs_return_flow_amount: Optional[float] = Field(alias="fbs_return_flow_amount", default=None)

    sales_percent_fbo: Optional[float] = Field(alias="sales_percent_fbo", default=None)

    sales_percent_fbs: Optional[float] = Field(alias="sales_percent_fbs", default=None)
