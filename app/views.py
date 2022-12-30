from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstview1(request):
    return HttpResponse('I Love My Family')