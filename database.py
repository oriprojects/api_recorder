##############################################################################
#                                   Imports                                  #
##############################################################################
import streamlit as st
from deta import Deta
from typing import List, Dict, Any
from endpoints_records import Record

# DATABASE SETTING
deta = Deta(st.secrets["API_RECORDER"]["DETA_KEY"])
db = deta.Base(st.secrets["API_RECORDER"]["DETA_BASE"])


def save_api_record(api_record: Dict[str, Record]) -> Any:
    """Return a response for the entity creation. Otherwise, raise an error"""
    return db.put(api_record)


def fetch_all_records() -> List[Dict[str, Record]]:
    """Return a list of dictionaries of all API records."""
    return db.fetch().items


def get_records_by_column_value(column_name: str, value: str) \
        -> List[Dict[str, Record]]:
    """Return a list dictionaries of API records with a specific API routing."""
    return [record for record in fetch_all_records()
            if record.get(column_name) == value]
