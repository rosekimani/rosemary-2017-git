from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<p>welcome to Akirachix class</p>")
def students(request):
    return HttpResponse("<p>welcome to Akirachix class</p>")
def teachers(request):
    return HttpResponse("<p>Here we will show all teachers</p>")