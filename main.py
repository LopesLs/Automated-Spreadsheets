import os

from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import gspread

load_dotenv()

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]

credentials = Credentials.from_service_account_file(
    "credentials.json", scopes=scopes
)

client = gspread.authorize(credentials)

sheet_id = os.getenv("SPREADSHEET_ID")

sheet = client.open_by_key(sheet_id)

worksheet = sheet.sheet1

# worksheet.update_title("A Spreadsheet")

# worksheet.update_cell(1, 1, "Hello World!")

# acess_value = worksheet.cell(1, 1).value

# find_value = worksheet.find("Hello World!")

# worksheet.format("A1", {"textFormat": {"bold": True}})