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
