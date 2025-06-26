# schedule
# A simple to use API for scheduling jobs
# Very lightweight and no external dependencies.

import schedule
import datetime


def my_job():
    print(f"I am exploring scheduling....")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

schedule.every(3).seconds.do(my_job)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
while True:
    schedule.run_pending()
    time.sleep(1)