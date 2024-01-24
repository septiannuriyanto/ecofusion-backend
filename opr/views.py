from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def init_opr(request):
    return HttpResponse('OPR')
