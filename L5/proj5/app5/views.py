from django.shortcuts import render
from app5 import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):

        registered=False

        if request.method == "POST":
            user_form = forms.UserForm(request.POST)
            profile_form = forms.UserProfileInfoForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():

                user = user_form.save()
                #Hash the password. Without this, hashing algorithm is not applied and password is not saved
                user.set_password(user.password)
                user.save()

                #commit = false does NOT save into database
                #Without this, the code breaks because profile.user is NULL
                profile = profile_form.save(commit=False)
                #one-to-one relation with user. We dont apply this in the form field
                profile.user = user

                #Without this, the image is not saved in the directory nor shown in the admin
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True
            else:
                print(user_form.errors,profile_form.errors)

        else:
                user_form = forms.UserForm()
                profile_form = forms.UserProfileInfoForm()

        return render(request,'registration.html',
                             {'registered':registered,
                              'user_form':user_form,
                              'profile_form':profile_form})


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
#reverse(name) does the samething as {% url 'name'%}
from django.urls import reverse
# Upon decorating, this view requires the user to be logged in to render
from django.contrib.auth.decorators import login_required

def user_login(request):#renders login.html or redirects to homepage on login

    if request.method == 'POST':
        #Get the fields
        username = request.POST.get('username')#login.html has a form with field names 'username'
        password = request.POST.get('password')

        #Authenticates the password for the user
        #This return variable can be accessed across all HTML templates!
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                #The user remains logged in across the whole project
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print(username, " tried to login with password ", password)
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'login.html')


#This code breaks if there is no login
@login_required
def user_logout(request):
    #The user is not logged out until this link is clicked
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
