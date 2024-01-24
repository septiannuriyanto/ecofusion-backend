from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def init_hokage(request):
    return HttpResponse('Hokage')
