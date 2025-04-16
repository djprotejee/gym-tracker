from datetime import datetime

def is_gym_open():
    now = datetime.now()
    weekday = now.weekday()  # 0=Mon, 6=Sun
    hour = now.hour

    if weekday < 5:
        return 7 <= hour < 22  # Weekdays: 7–22
    else:
        return 9 <= hour < 18  # Weekends: 9–18
