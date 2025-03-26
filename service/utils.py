from datetime import datetime
from zoneinfo import ZoneInfo

def get_thai_time(format: str = "%d-%m-%Y %H:%M:%S"):
    time = datetime.now(ZoneInfo('Asia/Bangkok'))
    return time.strftime(format)
