import schedule
import time

def greet(name):
    print("Hello", name)

schedule.every(3).seconds.do(greet, name = "Bob")
schedule.every(5).seconds.do(greet, name = "Nike")

while True:
    schedule.run_pending()
    time.sleep(1)