from simpleapp import views
from django.urls import path

urlpatterns = [
    path('', views.view_info)
]
