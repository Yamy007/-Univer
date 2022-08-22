from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h4>МОЖНА МЕНІ 5 </h4>")

def about(request):
    return  HttpResponse("<h1>about</h1>")

def information(requset):
    return  HttpResponse("<h1>information</h1>")


def FLXhomevorwk(request):
    return render(request, 'pages/home.html')