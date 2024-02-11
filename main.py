import os

from dotenv import load_dotenv

from utils import authenticate, get_spreadsheet

load_dotenv()

client = authenticate(
    ["https://www.googleapis.com/auth/spreadsheets"],
)

spreadsheet = get_spreadsheet(client, os.getenv("SPREADSHEET_ID"))

worksheet = spreadsheet.sheet1

# worksheet.update_title("A Spreadsheet")

# worksheet.update_cell(1, 1, "Hello World!")

# acess_value = worksheet.cell(1, 1).value

# find_value = worksheet.find("Hello World!")

# worksheet.format("A1", {"textFormat": {"bold": True}})
