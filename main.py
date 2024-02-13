import os

from dotenv import load_dotenv

from utils import authenticate, get_spreadsheet


def main():
    load_dotenv()  # Load environment variables from .env file

    if not os.getenv("SPREADSHEET_ID"):
        raise EnvironmentError("SPREADSHEET_ID not found in .env file")

    try:
        client = authenticate(
            ["https://www.googleapis.com/auth/spreadsheets"],
        )
    except Exception as e:
        print(f"Error authenticating with Google Sheets API: {e}")
        return

    spreadsheet = get_spreadsheet(client, os.getenv("SPREADSHEET_ID"))

    worksheet = spreadsheet.sheet1

    # Some examples of what you can do with the worksheet
    # worksheet.update_title("A Spreadsheet")
    # worksheet.update_cell(1, 1, "Hello World!")
    # acess_value = worksheet.cell(1, 1).value
    # find_value = worksheet.find("Hello World!")
    # worksheet.format("A1", {"textFormat": {"bold": True}})


if __name__ == "__main__":
    main()
