from django.shortcuts import render
from app3 import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    form = forms.SignUp_Form()

    if request.method == 'POST':
        form = forms.SignUp_Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'index.html')

    return render(request,'signup.html',context={'form':form})
