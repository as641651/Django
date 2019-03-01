from django.shortcuts import render
from app2.models import User

# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def users(request):
    user_list = User.objects.all()
    user_dict = {'users' : user_list}
    return render(request,'users.html',context=user_dict)
