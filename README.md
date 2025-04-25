# 🏋️ Gym Tracker

A fully automated gym occupancy tracker for [Total Fitness](https://totalfitness.com.ua/).  
It logs the number of active people in all gym locations every 15 (or any number) minutes and writes the data to:

- 📄 Local CSV file (`data/gym_data.csv`)
- 🟢 Google Sheets (via API)

---

## 📦 Features

- ✅ Tracks people count in **16+ gyms** across Ukraine
- ✅ Smart address & city matching (even when split across UI lines)
- ✅ Logs unknown gyms for manual review
- ✅ Auto-login via secure credentials
- ✅ Supports:
  - 💻 Local runners with Task Scheduler
  - ☁️ GitHub Actions for 24/7 cloud scraping
- ✅ Failsafe screenshot + logging in case of issues

---

## 📊 Sample Output

| timestamp           | city         | address         | active_people |
|---------------------|--------------|------------------|----------------|
| 2025-04-13 17:00:00 | Київ         | Жилянська        | 86             |
| 2025-04-13 17:00:00 | Львів        | Стрийська        | 62             |
| 2025-04-13 17:00:00 | Черкаси      | Смілянська       | 39             |

---

## 🛠 Installation

1. **Clone the repo**  
```bash
git clone https://github.com/djprotejee/gym-tracker.git
cd gym-tracker
```

2. **Create virtual environment**  
```bash
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/mac
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set environment variables**  
Create a `.env` file:

```env
GYM_EMAIL=your_email_here
GYM_PASSWORD=your_password_here
GOOGLE_CREDS_FILE=credentials.json
```

> 🔐 You’ll also need to set up a Google Service Account and download `credentials.json`.

---

## 🚀 Running

```bash
python main.py
```

This will:
- Log in to the website
- Collect data for all gyms
- Write to CSV and Google Sheets

---

## ☁️ GitHub Actions (Cloud Automation)

Gym Tracker can be run entirely in the cloud — no PC needed.

1. Go to **Settings → Secrets and Variables → Actions**
2. Add the following repository secrets:
   - `GYM_EMAIL`
   - `GYM_PASSWORD`
   - `GOOGLE_CREDS_BASE64` — your base64-encoded `credentials.json`
3. View/edit the schedule in `.github/workflows/scrape.yml`  
   The scraper only runs **during gym hours**:
   - **Weekdays:** 07:00–22:05
   - **Weekends:** 09:00–18:05

> ✅ Logs and screenshots are uploaded as GitHub Actions artifacts.

---

## 🖥 Automate Locally (Task Scheduler on Windows)

1. Use:
   - `run_scraper.bat` — visible runner
   - `run_silent.vbs` — background runner

2. Create a **Task Scheduler task**:
   - Trigger: every 15 minutes
   - Action: run `run_silent.vbs`
   - "Start in": full path to your project directory

3. Logs will be saved in `data/log.txt`, errors in `failures.log`.

> 💡 Perfect for fully offline, headless operation on your PC.

---

## 📁 Project Structure

```
gym-tracker/
├── .github/
│   └── workflows/
│       └── scrape.yml     # GitHub Actions workflow (cloud runner)
├── data/                  # Contains gym_data.csv, logs, etc.
│   ├── gym_data.csv
│   ├── failures.log
│   ├── unknown_gyms.log
│   └── log.txt
├── known_gyms.py          # Predefined (address, city) pairs
├── scraper.py             # Selenium logic for login & parsing
├── sheets_writer.py       # Google Sheets writer
├── logger.py              # Logging orchestrator
├── utils.py               # Helper: is_gym_open()
├── main.py                # Entry point
├── run_scraper.bat        # Manual runner
├── run_silent.vbs         # Background runner
├── .env                   # Environment variables
├── requirements.txt
└── README.md
```

---

## 📌 Version History

| Version | Highlights                                              |
|---------|---------------------------------------------------------|
| `v1.0`  | Initial version for Стрийська, Львів only               |
| `v1.1`  | 🆕 Support for all 16+ gyms, improved city/address matching |
| `v1.2`  | 🧾 Local automation (.bat + .vbs) and unified logging   |
| `v1.3`  | ☁️ GitHub Actions, smart scheduling and logging |

---

## 🧩 Tech Stack

- 🐍 Python 3.11+
- 📦 Selenium (headless Chrome)
- 🌐 Google Sheets API (`gspread`)
- 🗃 dotenv, cron, base64 secrets

---

## 🤝 Contributing

Pull requests are welcome!  
If you find a new gym not matched, just add it to `known_gyms.py`.

---

## 📜 License

MIT License. Just don't DDOS the gym site please
