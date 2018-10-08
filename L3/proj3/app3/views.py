from django.shortcuts import render
from app3 import forms

# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        do_something_with_data(form)

    return render(request,'form_page.html',context={'form':form})

def do_something_with_data(form):

    if form.is_valid(): ## Validates form

        # Do Something
        print("Validation success")

        # Access the data
        name = form.cleaned_data['name']
        print("NAME :", name)

        email = form.cleaned_data['email']
        print("Email :", email)

        text = form.cleaned_data['text']
        print("Text :", text)


def form_signUp_view(request):
    form = forms.Form_SignUp()

    if request.method == 'POST':
        form = forms.Form_SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("Invalid")

    return render(request,'form_page2.html',context={'form':form})
