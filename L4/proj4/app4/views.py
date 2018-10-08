from django.shortcuts import render
from app4 import forms

# Create your views here.
def index(request):
    d = {'text':'hello world',
         'number':100,
         'input':forms.NameForm()
        }
    return render(request,'index.html',context=d)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url_template.html')
