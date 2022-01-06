from django.http.response import HttpResponse
from django.shortcuts import render

def homeView(request):
    return HttpResponse('<h1>Home Page</h1>')