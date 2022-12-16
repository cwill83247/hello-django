from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request): # take a http request from user
    return HttpResponse("hello moto")    #returns a http resonse to user  neede to import http response at top  
