from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

def ping():
    print("Pinging every 10 seconds...")

scheduler = BlockingScheduler()

end_time = datetime.now() + timedelta(minutes=1)
scheduler.add_job(ping, 'interval', seconds=10, end_date=end_time)

scheduler.start()
