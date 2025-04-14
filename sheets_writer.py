import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Підключення до Google Sheets
def connect():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_file = os.getenv("GOOGLE_CREDS_FILE", "credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open("GymTracker").sheet1  # Назва таблиці
    return sheet

# Запис у таблицю
def write_to_google_sheets(city, address, people_count, timestamp):
    sheet = connect()
    sheet.append_row([timestamp, city, address, people_count])
    print(f"✅ Logged to Google Sheets: {city} — {address} — {people_count} людей")