import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def pass_list(
    data: ArrivalpassArrivalPassListRequest, api_config_override: Optional[APIConfig] = None
) -> ArrivalpassArrivalPassListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/pass/list"
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
                ArrivalpassArrivalPassListResponse(**response)
                if response is not None
                else ArrivalpassArrivalPassListResponse()
            )


async def carriage_pass_create(
    data: SellerSellerAPIArrivalPassCreateRequest, api_config_override: Optional[APIConfig] = None
) -> SellerSellerAPIArrivalPassCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/carriage/pass/create"
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
                SellerSellerAPIArrivalPassCreateResponse(**response)
                if response is not None
                else SellerSellerAPIArrivalPassCreateResponse()
            )


async def carriage_pass_update(
    data: SellerSellerAPIArrivalPassUpdateRequest, api_config_override: Optional[APIConfig] = None
) -> V1CarriagePassUpdatePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/carriage/pass/update"
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
                V1CarriagePassUpdatePostResponse(**response)
                if response is not None
                else V1CarriagePassUpdatePostResponse()
            )


async def carriage_pass_delete(
    data: SellerSellerAPIArrivalPassDeleteRequest, api_config_override: Optional[APIConfig] = None
) -> V1CarriagePassDeletePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/carriage/pass/delete"
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
                V1CarriagePassDeletePostResponse(**response)
                if response is not None
                else V1CarriagePassDeletePostResponse()
            )


async def return_pass_create(
    data: ArrivalpassArrivalPassCreateRequest, api_config_override: Optional[APIConfig] = None
) -> ArrivalpassArrivalPassCreateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/return/pass/create"
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
                ArrivalpassArrivalPassCreateResponse(**response)
                if response is not None
                else ArrivalpassArrivalPassCreateResponse()
            )


async def return_pass_update(
    data: ArrivalpassArrivalPassUpdateRequest, api_config_override: Optional[APIConfig] = None
) -> V1ReturnPassUpdatePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/return/pass/update"
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
                V1ReturnPassUpdatePostResponse(**response) if response is not None else V1ReturnPassUpdatePostResponse()
            )


async def return_pass_delete(
    data: ArrivalpassArrivalPassDeleteRequest, api_config_override: Optional[APIConfig] = None
) -> V1ReturnPassDeletePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/return/pass/delete"
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
                V1ReturnPassDeletePostResponse(**response) if response is not None else V1ReturnPassDeletePostResponse()
            )
