from datetime import datetime, timedelta

def calculate_delay_until_next_datetime(start_datetime):
    now = datetime.now()
    target_datetime = start_datetime

    if target_datetime <= now:
        delta_days = (target_datetime.weekday() - now.weekday()) % 7
        target_datetime += timedelta(days=delta_days)

    return target_datetime


