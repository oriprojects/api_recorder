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
API_RECORDER_SECRETS = st.secrets["API_RECORDER"]["DETA_DB_INFO"]
deta = Deta(API_RECORDER_SECRETS[0])
db = deta.Base(API_RECORDER_SECRETS[1])


def insert_api_record(api_record: Any) -> Any:
    """Returns the report on a successful entity creation,
     otherwise raises an error"""
    return db.put(dict(zip(COLUMNS_NAMES, api_record)))


def fetch_all_records() -> List[Record]:
    """Return a dictionary of all api records"""
    return db.fetch().items


def get_records_by_route(route: str) -> List[Record]:
    """Returns a dictionary of api records with a specific api routing"""
    return [record for record in fetch_all_records()
            if record.get("api_route") == route]
