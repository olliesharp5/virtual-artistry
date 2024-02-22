from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    return HttpResponse("The Help Page")