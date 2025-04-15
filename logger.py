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
    failures_path = os.path.join("data", "failures.log")
    unknown_path = os.path.join("data", "unknown_gyms.log")
    file_exists = os.path.isfile(filepath)

    success_count = 0
    failure_count = 0

    print("=" * 70)
    print(f"🕒 New logging session: {now}")
    print("=" * 70)

    with open(filepath, "a", newline="", encoding="utf-8") as f_csv, \
         open(failures_path, "a", encoding="utf-8") as log_fail, \
         open(unknown_path, "a", encoding="utf-8") as unknown_log:

        writer = csv.writer(f_csv)

        if not file_exists:
            writer.writerow(["timestamp", "city", "address", "active_people"])

        for gym in all_gyms:
            city = gym["city"]
            address = gym["address"]
            count = gym["count"]

            try:
                writer.writerow([now, city, address, count])
            except Exception as e:
                msg = f"[{now}] ❌ CSV error for {city} — {address}: {e}\n"
                log_fail.write(msg)
                print(msg.strip())
                failure_count += 1
                continue

            try:
                write_to_google_sheets(city, address, count, now)
                print(f"✅ Logged: [{now}] {city} — {address} — {count} людей → Google Sheets, CSV")
                success_count += 1
            except Exception as e:
                msg = f"[{now}] ❌ Google Sheets error for {city} — {address}: {e}\n"
                log_fail.write(msg)
                print(msg.strip())
                failure_count += 1

            # Log unknown gyms if applicable
            if city == "Невідомо":
                unknown_log.write(f"[{now}] {address}\n")

    print(f"📊 Logging summary: {success_count} success, {failure_count} failed")
    if failure_count > 0:
        print("⚠️ See 'data/failures.log' for details.")
