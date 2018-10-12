from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView,TemplateView
from . import forms

# Create your views here.
#accounts/signup/
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/signup.html'
