import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def rating_api_rating_summary_v1(
    data: V1empty, api_config_override: Optional[APIConfig] = None
) -> V1ratingSummaryV1response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/rating/summary"
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

            return V1ratingSummaryV1response(**response) if response is not None else V1ratingSummaryV1response()


async def rating_api_rating_history_v1(
    data: V1ratingHistoryV1request, api_config_override: Optional[APIConfig] = None
) -> V1ratingHistoryV1response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/rating/history"
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

            return V1ratingHistoryV1response(**response) if response is not None else V1ratingHistoryV1response()
