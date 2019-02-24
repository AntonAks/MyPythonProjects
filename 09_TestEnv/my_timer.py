import datetime

def timer_stop(h=17, m=0):
    result = False
    stop_time = datetime.datetime(year=datetime.datetime.now().year,
                                    month=datetime.datetime.now().month,
                                    day=datetime.datetime.now().day,
                                    hour=int(h),
                                    minute=int(m))

    if datetime.datetime.now() - stop_time >= datetime.timedelta(minutes=1):
        result = True
    return result

print(timer_stop())
