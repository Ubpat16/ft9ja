import schedule
import threading
import time
from .metaapi import get_data
import asyncio
import datetime as dt
from datetime import timedelta
from .models import DjangularDB

def run_continuously():
    cease_continuous_run = threading.Event()
    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def refresh_data(request):
    market_time = (dt.datetime.now() + timedelta(hours=2)).time().strftime('%H:%M:%S')
    info = asyncio.run(get_data())
    create_info = DjangularDB(market_watch_time=market_time, balance=info['balance'], equity=info['equity'])
    create_info.save()

schedule.every(5).minutes.do(refresh_data, request=None)
stop_run_continuously = run_continuously()
time.sleep(2)