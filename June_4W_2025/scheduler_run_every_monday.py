from apscheduler.schedulers.blocking import BlockingScheduler

def weekly_report():
    print("Sending weekly report email...")

scheduler = BlockingScheduler()
scheduler.add_job(weekly_report, 'cron', day_of_week='mon', hour=10, minute=30)
scheduler.start()
