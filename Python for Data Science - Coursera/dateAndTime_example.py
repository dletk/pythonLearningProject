import datetime as dt
import time

if __name__ == '__main__':
    now = time.time()
    timeByDate = dt.datetime.fromtimestamp(now)
    print(now)
    print(timeByDate)
    delta = dt.timedelta(days=100)
    today = dt.date.today()
    print(today-delta)