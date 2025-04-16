from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from known_gyms import GYMS
import os
import time

load_dotenv()

def normalize(text):
    # Normalize text: lowercase + remove dots, commas, extra prefixes like "вул", "пр-т"
    return (
        text.lower()
        .replace(",", "")
        .replace(".", "")
        .replace("вул", "")
        .replace("вулиця", "")
        .replace("пр-т", "")
        .replace("просп", "")
        .strip()
    )

def get_gym_people_list():
    # Load credentials from environment
    email = os.getenv("GYM_EMAIL")
    password = os.getenv("GYM_PASSWORD")

    # Configure headless Chrome
    options = Options()
    options.add_argument("--headless")  # comment out to see the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=uk-UA")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    gyms = []
    unknown_gyms = []

    try:
        # Step 1: Login to site
        print("\n[1] Logging in...")
        driver.get("https://totalfitness-ua.perfectgym.com/ClientPortal2/#/Login")
        time.sleep(5)

        driver.find_element(By.NAME, "Login").send_keys(email)
        driver.find_element(By.NAME, "Password").send_keys(password)
        driver.find_element(By.ID, "confirm").click()
        time.sleep(5)

        # Step 2: Navigate to page with club occupancy
        print("[2] Navigating to members page...")
        driver.get("https://totalfitness-ua.perfectgym.com/ClientPortal2/#/Clubs/MembersInClubs")
        time.sleep(5)

        driver.save_screenshot("debug.png") # DEBUG

        # Step 3: Parse all visible club blocks
        print("[3] Scraping clubs...")
        clubs = driver.find_elements(By.CLASS_NAME, "club-wrapper")

        for club in clubs:
            try:
                # Split all lines in the club block
                lines = club.text.split("\n")
                raw_name = lines[0].strip()
                name = raw_name.lstrip("0123456789. ").strip()
                address_line = lines[1].strip()  # full address string
                count_line = next(line for line in lines if "Зараз у клубі" in line or "Now In Club" in line)
                count = int(count_line.split(":")[-1].strip())

                # Try to match to known gyms by (address, city) with normalized text
                norm_name = normalize(name)
                norm_address_line = normalize(address_line)

                matched = False
                for known_address, known_city in GYMS:
                    if (
                            normalize(known_address) in norm_name or normalize(known_address) in norm_address_line
                    ) and (
                            normalize(known_city) in norm_name or normalize(known_city) in norm_address_line
                    ):
                        gyms.append({
                            "city": known_city,
                            "address": known_address,
                            "count": count
                        })
                        matched = True
                        break

                # If not matched — log and mark as unknown
                if not matched:
                    unknown_gyms.append((name, address_line))
                    gyms.append({
                        "city": "Невідомо",
                        "address": name,
                        "count": count
                    })

            except Exception as e:
                print("⚠️ Could not parse a club:", e)

        # Show list of clubs not matched to GYMS
        if unknown_gyms:
            print("\n🔍 Unknown gyms found:")
            for unknown in unknown_gyms:
                print(f" - {unknown[0]} / {unknown[1]}")

        return gyms

    except Exception as e:
        print("❌ Error:", e)
        return []

    finally:
        driver.quit()
