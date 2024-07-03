from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def display(request):
    return HttpResponse("<h1>MY FIrst Django APP</h1>")

def date_time(request):
    dt=datetime.datetime.now()
    s="<b>Current Date and Time:<b>"+str(dt)
    return HttpResponse(s)

