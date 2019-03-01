from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    helpDict = {'help_insert':"HELP PAGE"}
    return render(request,'help.html',context=helpDict)
