import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def cancellation_api_get_conditional_cancellation(
    data: V1getConditionalCancellationRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getConditionalCancellationResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/conditional-cancellation/get"
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
                V1getConditionalCancellationResponse(**response)
                if response is not None
                else V1getConditionalCancellationResponse()
            )


async def cancellation_api_get_conditional_cancellation_list_v2(
    data: V2getConditionalCancellationListV2request, api_config_override: Optional[APIConfig] = None
) -> V2getConditionalCancellationListV2response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/conditional-cancellation/list"
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
                V2getConditionalCancellationListV2response(**response)
                if response is not None
                else V2getConditionalCancellationListV2response()
            )


async def cancellation_api_get_conditional_cancellation_list(
    data: V1getConditionalCancellationListRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getConditionalCancellationListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/conditional-cancellation/list"
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
                V1getConditionalCancellationListResponse(**response)
                if response is not None
                else V1getConditionalCancellationListResponse()
            )


async def cancellation_api_conditional_cancellation_approve_v2(
    data: V2conditionalCancellationMoveV2request, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/conditional-cancellation/approve"
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

            return None


async def cancellation_api_conditional_cancellation_approve(
    data: V1conditionalCancellationMoveRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1empty:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/conditional-cancellation/approve"
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

            return V1empty(**response) if response is not None else V1empty()


async def cancellation_api_conditional_cancellation_reject_v2(
    data: V2conditionalCancellationMoveV2request, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/conditional-cancellation/reject"
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

            return None


async def cancellation_api_conditional_cancellation_reject(
    data: V1conditionalCancellationMoveRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1empty:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/conditional-cancellation/reject"
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

            return V1empty(**response) if response is not None else V1empty()
