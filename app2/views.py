from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_function(request):
    return HttpResponse('<h1>this is app2 function</>')