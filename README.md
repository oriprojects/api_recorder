# API Recorder

An application that interacts with APIs, stores their responses in a NoSQL database, and keeps a history of all past requests.

## Key Features

The page is divided into two components:

1. **Endpoint Entity**:
   In this option, you can insert a remote API route. If the request is successfully processed, a table containing all past records of this endpoint will be shown. Otherwise, an error window will appear with the relevant error.

2. **Endpoints History**:
   In this option, a table containing all past records from the database will be displayed.

A filtered table from the "Endpoints History" appears in the "Endpoint Entity" section.

## Usage

1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the application with `streamlit run app.py`.

## Code Bases

- `app.py`: Frontend code using Streamlit for the user interface.
- `database.py`: Backend code for interacting with the database.
- `endpoints_records.py`: Code for handling the creation of remote API records.

## Main Libraries

- Frontend: Streamlit, Pandas
- Backend: Deta (database connection)