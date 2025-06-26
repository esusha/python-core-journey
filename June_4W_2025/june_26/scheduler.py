# schedule
# A simple to use API for scheduling jobs
# Very lightweight and no external dependencies.

import schedule
import time

def my_job():
    print(f"I am exploring scheduling....")

schedule.every(3).seconds.do(my_job)

while True:
    schedule.run_pending()