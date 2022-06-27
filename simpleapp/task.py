from celery import shared_task
from datetime import datetime as dt, timedelta
from simpleapp.models import DjangularDB
import asyncio
from simpleapp.metaapi import get_data

@shared_task
def metaapi():
    market_time = (dt.datetime.now() + timedelta(hours=2)).time().strftime('%H:%M:%S')
    info = asyncio.run(get_data())
    create_info = DjangularDB(market_watch_time=market_time, balance=info['balance'], equity=info['equity'])
    create_info.save()