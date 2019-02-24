from time import sleep
from datetime import datetime, timedelta





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
