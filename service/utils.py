from sqlalchemy import DateTime
from datetime import datetime
from zoneinfo import ZoneInfo

def get_thai_time(format: str = "%d-%m-%Y %H:%M:%S") -> DateTime:
    time = datetime.now(ZoneInfo('Asia/Bangkok'))
    return time.strftime(format)
