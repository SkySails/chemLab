import datetime


def time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')

def timeShort():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
