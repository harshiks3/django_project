from django.urls import path
from firstApp.views import display
from firstApp.views import date_time


urlpatterns = [
    path('hello/',display),
    path('datetime/',date_time),
]
