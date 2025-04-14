from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_gym_people_count():
    email = os.getenv("GYM_EMAIL")
    password = os.getenv("GYM_PASSWORD")

    options = Options()
    options.add_argument("--headless")  # comment out to see the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("[1] Opening login page...")
        driver.get("https://totalfitness-ua.perfectgym.com/ClientPortal2/#/Login")
        time.sleep(5)

        print("[2] Logging in...")
        driver.find_element(By.NAME, "Login").send_keys(email)
        driver.find_element(By.NAME, "Password").send_keys(password)
        driver.find_element(By.ID, "confirm").click()
        time.sleep(7)

        print("[3] Navigating to members page...")
        driver.get("https://totalfitness-ua.perfectgym.com/ClientPortal2/#/Clubs/MembersInClubs")
        time.sleep(5)

        print("[4] Looking for Стрийська...")
        clubs = driver.find_elements(By.CLASS_NAME, "club-wrapper")

        for club in clubs:
            if "Стрийська" in club.text:
                # Find the number inside <strong>
                try:
                    number_elem = club.find_element(By.TAG_NAME, "strong")
                    number = int(number_elem.text.strip())
                    print(f"✅ Found Стрийська with {number} people")
                    return number
                except Exception as e:
                    print("❌ Found Стрийська but couldn't read number:", e)
                    return None

        print("❌ Стрийська not found.")
        return None

    except Exception as e:
        print("❌ Error during scraping:", e)
        return None

    finally:
        driver.quit()
