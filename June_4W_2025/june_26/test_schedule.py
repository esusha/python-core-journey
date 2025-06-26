import schedule
import time

def job():
    print("Job running!")

schedule.every(1).seconds.do(job)

counter = 0
while True:
    counter += 1
    schedule.run_pending()
    # Comment/uncomment the next line to compare
    time.sleep(1)
    if counter % 1000000 == 0:
        print("Looped", counter, "times")
