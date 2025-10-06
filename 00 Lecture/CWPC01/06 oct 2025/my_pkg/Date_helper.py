from datetime import datetime , timedelta

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_days(days):
    return (datetime.now()+timedelta(days=days)).strftime("%Y-%m-%d")

def is_weekend():
    return datetime.now().weekday() >= 5