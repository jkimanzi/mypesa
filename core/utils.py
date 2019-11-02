from datetime import datetime


def get_timestamp():

    time_now = datetime.now()
    time_stamp = time_now.strftime("%Y%m%d%H%M%S")
    return time_stamp
