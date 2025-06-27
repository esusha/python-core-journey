from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print("Running every 5 seconds...")

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=5)
scheduler.start()
