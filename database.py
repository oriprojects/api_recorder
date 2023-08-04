##############################################################################
#                                   Imports                                  #
##############################################################################
from deta import Deta
import streamlit as st
from typing import List, Dict, Union, Any
Record = Union[str, Dict, int, List, str]
##############################################################################
#                                   Globals                                  #
##############################################################################
COLUMNS_NAMES = ("key", "api_route", "output", "status_code", "http_methods")

# DATABASE SETTING
deta = Deta(st.secrets["API_RECORDER"]["DETA_KEY"])
db = deta.Base(st.secrets["API_RECORDER"]["DETA_BASE"])


def save_api_record(api_record: Any) -> Any:
    """Return a response for the entity creation. Otherwise, raise an error"""
    return db.put(dict(zip(COLUMNS_NAMES, api_record)))


def fetch_all_records() -> List[Record]:
    """Return a dictionary of all API records."""
    return db.fetch().items


def get_records_by_route(route: str) -> List[Record]:
    """Return a dictionary of API records with a specific API routing."""
    return [record for record in fetch_all_records()
            if record.get("api_route") == route]
