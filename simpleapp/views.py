from django.http import JsonResponse
from .models import DjangularDB
from .serializers import DjangularDBSerializer
from rest_framework.decorators import api_view
from .task import get_data

# Create your views here.
@api_view(['GET'])
def view_info(request):

    view_data = DjangularDB.objects.all()
    serializer = DjangularDBSerializer(view_data, many=True)
    return JsonResponse(serializer.data, safe=False)

