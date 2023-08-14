from datetime import datetime

def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time

def get_current_day():
    current_day = datetime.now().strftime("%A")
    return current_day
