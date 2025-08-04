import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def supply_draft_api_draft_cluster_list(
    data: V1draftClusterListRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftClusterListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cluster/list"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1draftClusterListResponse(**response) if response is not None else V1draftClusterListResponse()


async def supply_draft_api_draft_get_warehouse_fbo_list(
    data: V1draftGetWarehouseFboListRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftGetWarehouseFboListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/warehouse/fbo/list"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1draftGetWarehouseFboListResponse(**response)
                if response is not None
                else V1draftGetWarehouseFboListResponse()
            )


async def supply_draft_api_draft_create(
    data: V1draftCreateRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/draft/create"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1draftCreateResponse(**response) if response is not None else V1draftCreateResponse()


async def supply_draft_api_draft_create_info(
    data: V1draftCreateInfoRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftCreateInfoResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/draft/create/info"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1draftCreateInfoResponse(**response) if response is not None else V1draftCreateInfoResponse()


async def supply_draft_api_draft_timeslot_info(
    data: V1draftTimeslotInfoRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftTimeslotInfoResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/draft/timeslot/info"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1draftTimeslotInfoResponse(**response) if response is not None else V1draftTimeslotInfoResponse()


async def supply_draft_api_draft_supply_create(
    data: V1draftSupplyCreateRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftSupplyCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/draft/supply/create"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1draftSupplyCreateResponse(**response) if response is not None else V1draftSupplyCreateResponse()


async def supply_draft_api_draft_supply_create_status(
    data: V1draftSupplyCreateStatusRequest, api_config_override: Optional[APIConfig] = None
) -> V1draftSupplyCreateStatusResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/draft/supply/create/status"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1draftSupplyCreateStatusResponse(**response)
                if response is not None
                else V1draftSupplyCreateStatusResponse()
            )


async def cargoes_api_cargoes_create(
    data: V1cargoesCreateRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1cargoesCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes/create"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesCreateResponse(**response) if response is not None else V1cargoesCreateResponse()


async def cargoes_api_cargoes_create_info(
    data: V1cargoesCreateInfoRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1cargoesCreateInfoResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes/create/info"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesCreateInfoResponse(**response) if response is not None else V1cargoesCreateInfoResponse()


async def cargoes_api_cargoes_delete(
    data: V1cargoesDeleteRequest, api_config_override: Optional[APIConfig] = None
) -> V1cargoesDeleteResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes/delete"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesDeleteResponse(**response) if response is not None else V1cargoesDeleteResponse()


async def cargoes_api_cargoes_delete_status(
    data: V1cargoesDeleteStatusRequest, api_config_override: Optional[APIConfig] = None
) -> V1cargoesDeleteStatusResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes/delete/status"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1cargoesDeleteStatusResponse(**response) if response is not None else V1cargoesDeleteStatusResponse()
            )


async def cargoes_api_cargoes_rules_get(
    data: V1cargoesRulesGetRequest, api_config_override: Optional[APIConfig] = None
) -> V1cargoesRulesGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes/rules/get"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesRulesGetResponse(**response) if response is not None else V1cargoesRulesGetResponse()


async def cargoes_api_cargoes_label_create(
    data: V1cargoesLabelCreateRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1cargoesLabelCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes-label/create"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesLabelCreateResponse(**response) if response is not None else V1cargoesLabelCreateResponse()


async def cargoes_api_cargoes_label_get(
    data: V1cargoesLabelGetRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1cargoesLabelGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes-label/get"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1cargoesLabelGetResponse(**response) if response is not None else V1cargoesLabelGetResponse()


async def cargoes_api_cargoes_label_file(
    Client_Id: Optional[str] = None, Api_Key: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/cargoes-label/file/{file_guid}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def supply_order_api_supply_order_cancel(
    data: V1supplyOrderCancelRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1supplyOrderCancelResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/supply-order/cancel"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return V1supplyOrderCancelResponse(**response) if response is not None else V1supplyOrderCancelResponse()


async def supply_order_api_supply_order_cancel_status(
    data: V1supplyOrderCancelStatusRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1supplyOrderCancelStatusResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/supply-order/cancel/status"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Client-Id": Client_Id,
        "Api-Key": Api_Key,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1supplyOrderCancelStatusResponse(**response)
                if response is not None
                else V1supplyOrderCancelStatusResponse()
            )


async def supply_order_api_supply_order_content_update(
    data: V1supplyOrderContentUpdateRequest, api_config_override: Optional[APIConfig] = None
) -> V1supplyOrderContentUpdateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/supply-order/content/update"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1supplyOrderContentUpdateResponse(**response)
                if response is not None
                else V1supplyOrderContentUpdateResponse()
            )


async def supply_order_api_supply_order_content_update_status(
    data: V1supplyOrderContentUpdateStatusRequest, api_config_override: Optional[APIConfig] = None
) -> V1supplyOrderContentUpdateStatusResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/supply-order/content/update/status"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                V1supplyOrderContentUpdateStatusResponse(**response)
                if response is not None
                else V1supplyOrderContentUpdateStatusResponse()
            )
