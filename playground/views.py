from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    print(request)
    return HttpResponse('hello world krishna sdfver')