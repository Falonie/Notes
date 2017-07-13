from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    dt_str = datetime.strptime(a, '%Y-%m-%d,%H:%M:%S')
    return dt_str.timestamp()