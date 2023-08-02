##############################################################################
#                                   Imports                                  #
##############################################################################
from streamlit_option_menu import option_menu
from database import *
from endpoints_records import create_api_record
import pandas as pd

# PAGE SETTINGS
page_title = "API Recorder"
page_icon = ":globe_with_meridians:"
layout = "centered"
st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title + " " + page_icon)

# NAVIGATION MENU
selected_option = option_menu(
    menu_title=None,
    options=["Endpoint Entry", "Endpoints Records"],
    icons=["pencil-fill", "database-fill"],
    orientation="horizontal",
)


def insert_route_record_to_db(route):
    """Insert a record to database. If the insertion is successful, it shows all
     records with the same API routing, otherwise a ValueError is raised."""

    try:
        record = create_api_record(route)
        insert_api_record(record)
        st.subheader("Records with the same endpoint entity")
        visualize_records(get_records_by_route(route))

    except ValueError as error:
        st.error(error)


def visualize_records(records):
    """Display a table containing given records"""
    st.table(pd.DataFrame(records))


if __name__ == '__main__':
    if selected_option == "Endpoint Entry":
        with st.form("endpoint_form", clear_on_submit=True):
            api_route = st.text_area("", placeholder="Enter a valid endpoint")
            submit_button = st.form_submit_button("Save Endpoint")

            if submit_button:
                insert_route_record_to_db(api_route)
    else:
        st.subheader("Records history")
        visualize_records(fetch_all_records())
