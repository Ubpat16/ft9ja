import asyncio
from django.db import models

# Create your models here.
class DjangularDB(models.Model):
    market_watch_time = models.TimeField()
    balance = models.FloatField()
    equity = models.FloatField()
