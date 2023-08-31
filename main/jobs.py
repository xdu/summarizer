from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from datetime import datetime
import os

from web.feed import update

def update_rss():
    update("https://www.rtl.lu/rss/headlines")

def start():

    if (os.environ.get("RUN_MAIN") is None) :
        scheduler = BackgroundScheduler()

        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(update_rss, "interval", minutes=30, id="rtl", 
                        replace_existing=True, misfire_grace_time=120)

        scheduler.start()
        print("Scheduler started.")
    
    print(os.environ.get("RUN_MAIN"))