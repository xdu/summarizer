from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
from datetime import datetime

from web.feed import update

def update_rss():
    update("https://www.rtl.lu/rss/headlines")

def start():

    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    register_events(scheduler)

    scheduler.add_job(update_rss, "interval", minutes=30, id="rtl", 
                      replace_existing=True, misfire_grace_time=120)

    scheduler.start()
    print("Scheduler started.")