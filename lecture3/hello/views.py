from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def baha(request):
    return HttpResponse("Hello, Baha!")

def varvara(request):
    return HttpResponse("Привет, Варвара!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()})
