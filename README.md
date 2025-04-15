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
- ✅ Designed to run on [Render](https://render.com) or any cloud platform
- ✅ Supports background logging on Windows via **Task Scheduler**

---

## 📊 Sample Output

| timestamp           | city         | address         | active_people |
|---------------------|--------------|------------------|----------------|
| 2025-04-13 17:00:00 | Київ         | Жилянська        | 17             |
| 2025-04-13 17:00:00 | Львів        | Стрийська        | 12             |
| 2025-04-13 17:00:00 | Черкаси      | Смілянська       | 8              |

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

## 🔁 Automate with Render

1. Deploy to [Render](https://render.com)
2. Use [cron jobs](https://render.com/docs/cronjobs) to run `main.py` every 10 minutes
3. Add your `.env` and `credentials.json` to the Render dashboard

---

## 🕒 Automate with Windows Task Scheduler

1. Use the provided `run_scraper.bat` or `run_silent.vbs`:
   - `run_scraper.bat` — opens terminal and logs visibly
   - `run_silent.vbs` — runs the `.bat` file silently in background

2. In Task Scheduler:
   - **Trigger:** every 15 minutes (or your choice)
   - **Action:** run `run_silent.vbs`
   - **Start in:** folder containing your `gym_scraper` project

3. Logs will be saved in `data/log.txt`, errors in `failures.log`.

> 💡 Perfect for fully offline, headless operation on your PC.

---

## 📁 Project Structure

```
gym-tracker/
├── data/                  # Contains gym_data.csv, logs, etc.
│   ├── gym_data.csv
│   ├── failures.log
│   ├── unknown_gyms.log
│   └── log.txt
├── known_gyms.py          # Predefined (address, city) pairs
├── scraper.py             # Selenium logic for login & parsing
├── sheets_writer.py       # Google Sheets writer
├── logger.py              # Logging orchestrator
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

---

## 🧩 Tech Stack

- 🐍 Python 3.11+
- 📦 Selenium
- 🌐 Google Sheets API (`gspread`)
- 🗃 dotenv, csv, Task Scheduler, Render

---

## 🤝 Contributing

Pull requests are welcome!  
If you find a new gym not matched, just add it to `known_gyms.py`.

---

## 📜 License

MIT License. Just don't DDOS the gym site please xD
