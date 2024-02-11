from google.oauth2.service_account import Credentials
import gspread

def authenticate(scopes: list[str]) -> gspread.Client:
    credentials = Credentials.from_service_account_file(
        "credentials.json", scopes=scopes
    )

    return gspread.authorize(credentials)

def get_spreadsheet(client: gspread.Client, sheet_id: str) -> gspread.Spreadsheet:
    return client.open_by_key(sheet_id)
