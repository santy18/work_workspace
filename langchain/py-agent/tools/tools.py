from langchain.tools import tool
import httpx
from config.itglue_config import token, ITGLUE_BASE_URL, IGLUE_API_URL
from urllib.parse import urlencode

# related=true&limit=50&query=a&filter_organization_id=517661&exclude_archived=true&include_personal_passwords=true

@tool
def search_itglue(path: str, filters: dict) -> str:
    """
    Search ITGlue assets by kind and query.
    path: path to search, e.g. "/search.json", "/organizations/{{organization_id}}/relationships/{{resource_type}}"
    filters: dictionary of filters to apply, e.g. {"related": "true", "limit": 50, "query": "a", "filter_organization_id": 517661}
    """
    
        # Use different base depending on the type of call
    if path == "/search.json":
        base_url = ITGLUE_BASE_URL
    else:
        base_url = IGLUE_API_URL

    url = base_url + path
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": token,
    }

    params = {
        "limit": filters.get("limit", 50),
        "boost_organization_id": filters.get("boost_organization_id", 517661),
        "query": filters.get("query", ""),
        "kind": filters.get("kind", ""),
    }

    try:
        print(f"TOOL CALL: Searching ITGlue for '{path}' with params '{params}'")
        response = httpx.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return str(response.json())[:1500]
    except Exception as e:
        return f"❌ API call failed: {e}"

def build_full_path(path: str, filters: dict) -> str:
    query_params = {}

    for k, v in filters.items():
        query_params[f"filter[{k}]"] = v

    # Optional: add pagination or sorting defaults
    query_params.update({
        "page[size]": 10,
        "page[number]": 1,
        "sort": "-name"
    })

    query_string = urlencode(query_params)
    return f"{path}?{query_string}" if query_params else path