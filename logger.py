from scraper import get_gym_people_count
from sheets_writer import write_to_google_sheets
from datetime import datetime
import csv
import os

def log_gym_data():
    city = "Львів"
    address = "Стрийська"
    count = get_gym_people_count()
    if count is None:
        return

    # Створити один timestamp для обох джерел
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ✅ Google Sheets
    write_to_google_sheets(city, address, count, now)

    # ✅ CSV
    filepath = os.path.join("data", "gym_data.csv")
    file_exists = os.path.isfile(filepath)

    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "city", "address", "active_people"])
        writer.writerow([now, city, address, count])

    print(f"[{now}] Logged: {city}, {address} — {count} people")
