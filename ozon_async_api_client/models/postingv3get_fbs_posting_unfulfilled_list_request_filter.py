from typing import *

from pydantic import BaseModel, Field


class Postingv3getFbsPostingUnfulfilledListRequestFilter(BaseModel):
    """
        object model

        Фильтр запроса.

    Используйте фильтр либо по времени сборки — `cutoff`, либо по дате передачи отправления в доставку — `delivering_date`.
    Если использовать их вместе, в ответе вернётся ошибка.

    Чтобы использовать фильтр по времени сборки, заполните поля `cutoff_from` и `cutoff_to`.

    Чтобы использовать фильтр по дате передачи отправления в доставку, заполните поля `delivering_date_from` и `delivering_date_to`.

    """

    cutoff_from: str = Field(alias="cutoff_from")

    cutoff_to: str = Field(alias="cutoff_to")

    delivering_date_from: Optional[str] = Field(alias="delivering_date_from", default=None)

    delivering_date_to: Optional[str] = Field(alias="delivering_date_to", default=None)

    delivery_method_id: Optional[List[int]] = Field(alias="delivery_method_id", default=None)

    is_quantum: Optional[bool] = Field(alias="is_quantum", default=None)

    provider_id: Optional[List[int]] = Field(alias="provider_id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    warehouse_id: Optional[List[int]] = Field(alias="warehouse_id", default=None)
