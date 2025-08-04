from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_status_v5response_product_exemplar_mark import \
    V5fbsPostingProductExemplarStatusV5responseProductExemplarMark


class V5fbsPostingProductExemplarStatusV5responseProductExemplar(BaseModel):
    """
    None model
    """

    exemplar_id: Optional[int] = Field(alias="exemplar_id", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    gtd_check_status: Optional[str] = Field(alias="gtd_check_status", default=None)

    gtd_error_codes: Optional[List[str]] = Field(alias="gtd_error_codes", default=None)

    is_gtd_absent: Optional[bool] = Field(alias="is_gtd_absent", default=None)

    is_rnpt_absent: Optional[bool] = Field(alias="is_rnpt_absent", default=None)

    marks: Optional[List[Optional[V5fbsPostingProductExemplarStatusV5responseProductExemplarMark]]] = Field(
        alias="marks", default=None
    )

    rnpt: Optional[str] = Field(alias="rnpt", default=None)

    rnpt_check_status: Optional[str] = Field(alias="rnpt_check_status", default=None)

    rnpt_error_codes: Optional[List[str]] = Field(alias="rnpt_error_codes", default=None)
