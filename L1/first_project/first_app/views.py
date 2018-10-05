from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     #request is an object from django.http
#     return HttpResponse("Hello World!")


def index(request):
    my_dict = { 'insert_me':"Hello I am from views.py"}
    return render(request,'first_app/index.html',context=my_dict)
