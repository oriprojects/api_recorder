##############################################################################
#                                   Imports                                  #
##############################################################################
from urllib.parse import urlparse
from datetime import datetime
import requests
from typing import List, Dict, Union
##############################################################################
#                                   Globals                                  #
##############################################################################
UNKNOWN_HTTP_METHODS = []
##############################################################################
#                                   Types                                    #
##############################################################################
Record = Union[str, Dict, int, List, str]


def is_url_format_valid(url: str) -> bool:
    """Check if the given URL has a valid format."""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)


def get_supported_http_methods(api_route: str) -> List[str]:
    """Get a list of all HTTP methods the API accepts. If the request was not
     accepted or an error occurred, return UNKNOWN_HTTP_METHODS variable."""
    try:
        response = requests.options(api_route)
        return response.headers.get("allow", "").split(", ")

    except requests.exceptions.RequestException:
        return UNKNOWN_HTTP_METHODS


def create_api_record(api_route: str) -> Record:
    """Create a comprehensive record for the given API routing. If the provided
    API isn't a valid URL or the server didn't accept the request, raise a
    ValueError message with the corresponding error."""
    if not is_url_format_valid(api_route):
        raise ValueError("Given API in not a valid URL")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    https_methods = get_supported_http_methods(api_route)

    try:
        response = requests.get(api_route)
        https_methods = ["GET"] if not https_methods else https_methods
        return current_time, api_route, response.json(), response.status_code,\
            https_methods

    except requests.exceptions.RequestException:
        return ValueError("A problem occurred during the request")
