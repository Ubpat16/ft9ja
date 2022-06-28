import asyncio
from django.http import HttpResponse, JsonResponse
from httpx import StatusCode
# from django.shortcuts import render
# from rest_framework.response import Response
from .models import DjangularDB
from .serializers import DjangularDBSerializer
from rest_framework.decorators import api_view
from .metaapi import get_data
import datetime as dt
from datetime import timedelta


# Create your views here.
@api_view(['GET'])
def view_info(request):

    view_data = DjangularDB.objects.all()
    serializer = DjangularDBSerializer(view_data, many=True)
    return JsonResponse(serializer.data, safe=False)


def refresh_data(request):
    market_time = (dt.datetime.now() + timedelta(hours=2)).time().strftime('%H:%M:%S')
    info = asyncio.run(get_data())
    create_info = DjangularDB(market_watch_time=market_time, balance=info['balance'], equity=info['equity'])
    create_info.save()
    return HttpResponse("Success")