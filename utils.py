from google.oauth2.service_account import Credentials
import gspread


def authenticate(scopes: list[str]) -> gspread.Client:
    """Authenticate user with Google Sheets API using service accoun credentials

    Args:
        `scopes (list[str])`: List of api scopes to authenticate with

    Returns:
        `gspread.Client`: Authenticate client ready to acess Google Sheets API
    """

    credentials = Credentials.from_service_account_file(
        "credentials.json", scopes=scopes
    )

    return gspread.authorize(credentials)


def get_spreadsheet(client: gspread.Client, spreadsheet_id: str) -> gspread.Spreadsheet:
    """Get a Google Sheets spreadsheet by its id

    Args:
        `client (gspread.Client)`: Authenticated client object
        `spreadsheet_id (str)`: Id of the spreadsheet to acess

    Returns:
        `gspread.Spreadsheet`: The spreadsheet object accesed by the id
    """

    return client.open_by_key(spreadsheet_id)
