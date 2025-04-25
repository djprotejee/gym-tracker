from datetime import datetime

def is_gym_open():
    now = datetime.now()
    weekday = now.weekday()  # 0 = Monday, 6 = Sunday
    hour = now.hour
    minute = now.minute

    if weekday < 5:
        # Weekdays: 07:00 – 22:05
        return (7 <= hour < 22) or (hour == 22 and minute <= 5)
    else:
        # Weekends: 09:00 – 18:05
        return (9 <= hour < 18) or (hour == 18 and minute <= 5)