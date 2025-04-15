import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Google Sheets
def connect():
    # Authenticate with Google Sheets using service account
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_file = os.getenv("GOOGLE_CREDS_FILE", "credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open("GymTracker").sheet1 # Spreadsheet name
    return sheet

# Append to sheet
def write_to_google_sheets(city, address, people_count, timestamp):
    # Append new row with current data
    sheet = connect()
    sheet.append_row([timestamp, city, address, people_count])