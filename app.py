##############################################################################
#                                   Imports                                  #
##############################################################################
import pandas as pd
from streamlit_option_menu import option_menu
from database import *
from endpoints_records import create_api_record

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


def display_records(records):
    """Display a table that contains the requested records"""
    st.table(pd.DataFrame(records))


def upload_route_record_to_db(route):
    """Upload an API record to the database. If the record exists, display a
     table of shared API routing records. Otherwise, raise ValueError with a
     relevant error."""

    try:
        record = create_api_record(route)
        save_api_record(record)
        st.subheader("API records")
        display_records(get_records_by_route(route))

    except ValueError as error:
        st.error(error)


if __name__ == '__main__':
    if selected_option == "Endpoint Entry":
        with st.form("endpoint_form", clear_on_submit=True):
            st.subheader("Select remote API endpoint")
            api_route = st.text_area("api_route", label_visibility="hidden",
                                     placeholder="Enter a valid endpoint")
            submit_button = st.form_submit_button("Save")

            if submit_button:
                upload_route_record_to_db(api_route)
    else:
        st.subheader("Database Records")
        display_records(fetch_all_records())
