import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def finance_api_get_realization_report_v2(
    data: V2getRealizationReportRequestV2,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V2getRealizationReportResponseV2:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/finance/realization"
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
                V2getRealizationReportResponseV2(**response)
                if response is not None
                else V2getRealizationReportResponseV2()
            )


async def finance_api_get_realization_report_v1(
    data: V1getRealizationReportPostingRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getRealizationReportPostingResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/realization/posting"
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
                V1getRealizationReportPostingResponse(**response)
                if response is not None
                else V1getRealizationReportPostingResponse()
            )


async def finance_api_finance_transaction_list_v3(
    data: Financev3financeTransactionListV3request,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Financev3financeTransactionListV3response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v3/finance/transaction/list"
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
                Financev3financeTransactionListV3response(**response)
                if response is not None
                else Financev3financeTransactionListV3response()
            )


async def finance_api_finance_transaction_total_v3(
    data: Financev3financeTransactionTotalsV3request,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Financev3financeTransactionTotalsV3response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v3/finance/transaction/totals"
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
                Financev3financeTransactionTotalsV3response(**response)
                if response is not None
                else Financev3financeTransactionTotalsV3response()
            )


async def report_api_create_document_b2bsales_report(
    data: V1createDocumentB2bSalesReportRequest, api_config_override: Optional[APIConfig] = None
) -> CommonCreateReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/document-b2b-sales"
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

            return CommonCreateReportResponse(**response) if response is not None else CommonCreateReportResponse()


async def report_api_create_document_b2bsales_jsonreport(
    data: V1createDocumentB2bSalesJSONReportRequest, api_config_override: Optional[APIConfig] = None
) -> V1createDocumentB2bSalesJSONReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/document-b2b-sales/json"
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
                V1createDocumentB2bSalesJSONReportResponse(**response)
                if response is not None
                else V1createDocumentB2bSalesJSONReportResponse()
            )


async def report_api_create_mutual_settlement_report(
    data: V1createMutualSettlementReportRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> CommonCreateReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/mutual-settlement"
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

            return CommonCreateReportResponse(**response) if response is not None else CommonCreateReportResponse()


async def finance_api_get_realization_by_day_report_v1(
    data: V1getRealizationReportByDayRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> GetRealizationReportByDayResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/realization/by-day"
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
                GetRealizationReportByDayResponse(**response)
                if response is not None
                else GetRealizationReportByDayResponse()
            )


async def get_finance_products_buyout(
    data: V1getFinanceProductsBuyoutRequest, api_config_override: Optional[APIConfig] = None
) -> V1getFinanceProductsBuyoutResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/products/buyout"
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
                V1getFinanceProductsBuyoutResponse(**response)
                if response is not None
                else V1getFinanceProductsBuyoutResponse()
            )


async def report_api_get_compensation_report(
    data: V1getCompensationReportRequest, api_config_override: Optional[APIConfig] = None
) -> CreateReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/compensation"
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

            return CreateReportResponse(**response) if response is not None else CreateReportResponse()


async def report_api_get_decompensation_report(
    data: V1getDecompensationReportRequest, api_config_override: Optional[APIConfig] = None
) -> CreateReportResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/finance/decompensation"
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

            return CreateReportResponse(**response) if response is not None else CreateReportResponse()
