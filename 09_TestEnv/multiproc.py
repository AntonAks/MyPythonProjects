from time import sleep
from datetime import datetime, timedelta
from multiprocessing import Process


def main_process():
    i = 0
    while True:
        i = i + 1
        print(i, datetime.now(), main_process.__str__(), )
        sleep(.3)

def secondary_process():
    i = 0
    while True:
        i = i + 1
        print(i, datetime.now(), secondary_process.__str__())
        sleep(1)


p_1 = Process(target=main_process, name='main_process')
p_2 = Process(target=secondary_process, name='secondary_process')


def timer_stop(h=0, m=0, p_list=[]):
    stop_time = datetime(year=datetime.now().year,
                                        month=datetime.now().month,
                                        day=datetime.now().day,
                                        hour=int(h),
                                        minute=int(m))

    print(datetime.now() - stop_time)

    for p in p_list:
        p.start()

    while True:

        if datetime.now() - stop_time > timedelta(minutes=0):
            for p in p_list:
                p.terminate()
                p.join()


timer_stop(16,14, p_list=[p_1, p_2])
