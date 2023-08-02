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
INVALID_RECORD = ()
##############################################################################
#                                   Types                                    #
##############################################################################
Record = Union[str, Dict, int, List, str]


def is_url_format_valid(url: str) -> bool:
    """Checks if the given url has a valid format."""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)


def get_supported_http_methods(api_route: str) -> List[str]:
    """Retrieves a list of all http methods that acceptable by the api. If the
    request was not accepted or an error occurred, return UNKNOWN_HTTP_METHODS
    variable."""
    try:
        response = requests.options(api_route)
        return response.headers.get("allow", "").split(", ")

    except requests.exceptions.RequestException:
        return UNKNOWN_HTTP_METHODS


def create_api_record(api_route: str) -> Record:
    """Creates a full detailed record for the given api routing. If the request
     was not accepted return INVALID_RECORD variable."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    https_methods = get_supported_http_methods(api_route)

    try:
        response = requests.get(api_route)
        https_methods = ["GET"] if not https_methods else https_methods
        return current_time, api_route, response.json(), response.status_code,\
            https_methods

    except requests.exceptions.RequestException:
        return INVALID_RECORD


def validate_api_record(api_route: str) -> \
        Dict[str, Union[str, Dict, int, List, str]]:
    """Validates api record. If it's not a record raise ValueError."""

    if not is_url_format_valid(api_route):
        raise ValueError("Given api in not a valid url")

    api_record = create_api_record(api_route)

    if not api_record:
        raise ValueError("A problem occurred during the request")

    return api_record
