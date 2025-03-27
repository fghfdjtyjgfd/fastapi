from datetime import datetime
import pytz

def get_thai_time():
    thai_timezone = pytz.timezone('Asia/Bangkok')
    utc_now = datetime.now(pytz.utc)
    thailand_time = utc_now.astimezone(thai_timezone)
    return thailand_time

# print(get_thai_time())