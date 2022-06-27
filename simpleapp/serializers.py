from pyexpat import model
from rest_framework import serializers
from .models import DjangularDB

class DjangularDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangularDB
        fields = ('market_watch_time', 'balance', 'equity')