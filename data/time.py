from datetime import datetime


def time_now():
    date_string = str(datetime.now())
    datetime_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
    formatted_date = datetime_obj.isoformat(timespec="milliseconds") + "Z"
    return formatted_date
