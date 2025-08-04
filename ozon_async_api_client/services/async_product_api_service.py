import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def product_api_import_products_v3(
    data: V3importProductsRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V3importProductsResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v3/product/import"
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

            return V3importProductsResponse(**response) if response is not None else V3importProductsResponse()


async def product_api_get_import_products_info(
    data: ProductGetImportProductsInfoRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ProductGetImportProductsInfoResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/import/info"
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
                ProductGetImportProductsInfoResponse(**response)
                if response is not None
                else ProductGetImportProductsInfoResponse()
            )


async def product_api_import_products_by_sku(
    data: ProductImportProductsBySKURequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ProductImportProductsBySKUResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/import-by-sku"
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
                ProductImportProductsBySKUResponse(**response)
                if response is not None
                else ProductImportProductsBySKUResponse()
            )


async def product_api_product_update_attributes(
    data: V1productUpdateAttributesRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productUpdateAttributesResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/attributes/update"
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
                V1productUpdateAttributesResponse(**response)
                if response is not None
                else V1productUpdateAttributesResponse()
            )


async def product_api_product_import_pictures(
    data: Productv1productImportPicturesRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Productv1productInfoPicturesResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/pictures/import"
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
                Productv1productInfoPicturesResponse(**response)
                if response is not None
                else Productv1productInfoPicturesResponse()
            )


async def product_api_get_product_list(
    data: Productv3getProductListRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Productv3getProductListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v3/product/list"
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
                Productv3getProductListResponse(**response)
                if response is not None
                else Productv3getProductListResponse()
            )


async def product_api_get_product_rating_by_sku(
    data: V1getProductRatingBySkuRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1getProductRatingBySkuResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/rating-by-sku"
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
                V1getProductRatingBySkuResponse(**response)
                if response is not None
                else V1getProductRatingBySkuResponse()
            )


async def product_api_get_product_info_list(
    data: V3getProductInfoListRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V3getProductInfoListResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v3/product/info/list"
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

            return V3getProductInfoListResponse(**response) if response is not None else V3getProductInfoListResponse()


async def product_api_get_product_attributes_v4(
    data: Productv4getProductAttributesV4request,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Productv4getProductAttributesV4response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v4/product/info/attributes"
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
                Productv4getProductAttributesV4response(**response)
                if response is not None
                else Productv4getProductAttributesV4response()
            )


async def product_api_get_product_info_description(
    data: ProductGetProductInfoDescriptionRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ProductGetProductInfoDescriptionResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/info/description"
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
                ProductGetProductInfoDescriptionResponse(**response)
                if response is not None
                else ProductGetProductInfoDescriptionResponse()
            )


async def product_api_get_upload_quota(
    data: V1empty,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V4getUploadQuotaResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v4/product/info/limit"
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

            return V4getUploadQuotaResponse(**response) if response is not None else V4getUploadQuotaResponse()


async def product_api_product_update_offer_id(
    data: V1productUpdateOfferIdRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productUpdateOfferIdResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/update/offer-id"
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
                V1productUpdateOfferIdResponse(**response) if response is not None else V1productUpdateOfferIdResponse()
            )


async def product_api_product_archive(
    data: ProductProductArchiveRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ProductBooleanResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/archive"
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

            return ProductBooleanResponse(**response) if response is not None else ProductBooleanResponse()


async def product_api_product_unarchive(
    data: ProductProductUnarchiveRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ProductBooleanResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/unarchive"
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

            return ProductBooleanResponse(**response) if response is not None else ProductBooleanResponse()


async def product_api_delete_products(
    data: Productv2deleteProductsRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Productv2deleteProductsResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/products/delete"
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
                Productv2deleteProductsResponse(**response)
                if response is not None
                else Productv2deleteProductsResponse()
            )


async def product_api_get_product_info_subscription(
    data: V1getProductInfoSubscriptionRequest, api_config_override: Optional[APIConfig] = None
) -> V1getProductInfoSubscriptionResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/info/subscription"
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
                V1getProductInfoSubscriptionResponse(**response)
                if response is not None
                else V1getProductInfoSubscriptionResponse()
            )


async def product_api_product_get_related_sku(
    data: V1productGetRelatedSKURequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V1productGetRelatedSKUResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v1/product/related-sku/get"
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
                V1productGetRelatedSKUResponse(**response) if response is not None else V1productGetRelatedSKUResponse()
            )


async def product_api_product_info_pictures_v2(
    data: V2productInfoPicturesRequest,
    Client_Id: Optional[str] = None,
    Api_Key: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> V2productInfoPicturesResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or ""
    path = f"/v2/product/pictures/info"
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
                V2productInfoPicturesResponse(**response) if response is not None else V2productInfoPicturesResponse()
            )
