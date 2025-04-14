from scraper import get_gym_people_list
from sheets_writer import write_to_google_sheets
from datetime import datetime
import csv
import os

def log_gym_data():
    # Get all gym data via scraper
    all_gyms = get_gym_people_list()
    if not all_gyms:
        print("❌ No data fetched")
        return

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filepath = os.path.join("data", "gym_data.csv")
    file_exists = os.path.isfile(filepath)

    # Open CSV file and write data
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "city", "address", "active_people"])

        for gym in all_gyms:
            writer.writerow([now, gym["city"], gym["address"], gym["count"]])
            write_to_google_sheets(gym["city"], gym["address"], gym["count"], now)

    print(f"✅ Logged {len(all_gyms)} gyms.")
