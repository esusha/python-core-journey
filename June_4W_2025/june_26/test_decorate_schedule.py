# Use the @repeat to schedule a function
from schedule import repeat, run_pending, every
import time, datetime

@repeat(every(5).seconds)
def sample_job():
    print("Hello running scheuled job")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
while True:
    run_pending()
    time.sleep(1)