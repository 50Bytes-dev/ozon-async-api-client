import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def analytics_api_manage_stocks(
    data: V1analyticsManageStocksRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1analyticsManageStocksResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/analytics/manage/stocks"
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
                V1analyticsManageStocksResponse(**response)
                if response is not None
                else V1analyticsManageStocksResponse()
            )


async def analytics_api_analytics_stocks(
    data: V1analyticsStocksRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1analyticsStocksResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/analytics/stocks"
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

            return V1analyticsStocksResponse(**response) if response is not None else V1analyticsStocksResponse()


async def analytics_api_average_delivery_time(
    data: V1averageDeliveryTimeRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1averageDeliveryTimeResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/analytics/average-delivery-time"
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
                V1averageDeliveryTimeResponse(**response) if response is not None else V1averageDeliveryTimeResponse()
            )


async def analytics_api_average_delivery_time_details(
    data: V1averageDeliveryTimeDetailsRequest, api_config_override: Optional[APIConfig] = None
) -> V1averageDeliveryTimeDetailsResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/analytics/average-delivery-time/details"
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
                V1averageDeliveryTimeDetailsResponse(**response)
                if response is not None
                else V1averageDeliveryTimeDetailsResponse()
            )


async def average_delivery_time_summary(
    Client_Id: Optional[str] = None, Api_Key: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> V1averageDeliveryTimeSummaryResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/analytics/average-delivery-time/summary"
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
            "post",
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

            return (
                V1averageDeliveryTimeSummaryResponse(**response)
                if response is not None
                else V1averageDeliveryTimeSummaryResponse()
            )


async def carriage_api_set_postings(
    data: V1setPostingsRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1setPostingsResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/carriage/set-postings"
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

            return V1setPostingsResponse(**response) if response is not None else V1setPostingsResponse()


async def carriage_api_carriage_cancel(
    data: V1carriageCancelRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1carriageCancelResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/carriage/cancel"
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

            return V1carriageCancelResponse(**response) if response is not None else V1carriageCancelResponse()


async def product_api_action_timer_update(
    data: V1productActionTimerUpdateRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productActionTimerUpdateResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/action/timer/update"
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
                V1productActionTimerUpdateResponse(**response)
                if response is not None
                else V1productActionTimerUpdateResponse()
            )


async def product_api_action_timer_status(
    data: V1productActionTimerStatusRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productActionTimerStatusResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/action/timer/status"
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
                V1productActionTimerStatusResponse(**response)
                if response is not None
                else V1productActionTimerStatusResponse()
            )


async def product_api_product_info_wrong_volume(
    data: V1productInfoWrongVolumeRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productInfoWrongVolumeResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/info/wrong-volume"
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
                V1productInfoWrongVolumeResponse(**response)
                if response is not None
                else V1productInfoWrongVolumeResponse()
            )


async def access_api_roles_by_token(
    data: V1empty,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1rolesByTokenResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/roles"
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

            return V1rolesByTokenResponse(**response) if response is not None else V1rolesByTokenResponse()


async def get_supply_returns_summary_report(
    data: V1getSupplyReturnsSummaryReportRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getSupplyReturnsSummaryReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/removal/from-supply/list"
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
                V1getSupplyReturnsSummaryReportResponse(**response)
                if response is not None
                else V1getSupplyReturnsSummaryReportResponse()
            )


async def get_supplier_returns_summary_report(
    data: V1getSupplierReturnsSummaryReportRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getSupplierReturnsSummaryReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/removal/from-stock/list"
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
                V1getSupplierReturnsSummaryReportResponse(**response)
                if response is not None
                else V1getSupplierReturnsSummaryReportResponse()
            )
