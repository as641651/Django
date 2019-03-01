from django.shortcuts import render
from app3 import forms
from django.http import HttpResponseRedirect
#reverse(name) does the samething as {% url 'name'%}
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    form = forms.SignUp_Form()

    if request.method == 'POST':
        form = forms.SignUp_Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return render(request,'index.html')
            #use redirect instead of render when navigating to someother site (L5)
            #render does not change the url. ie url of index page will be url of this page
            return HttpResponseRedirect(reverse('index'))

    return render(request,'signup.html',context={'form':form})
