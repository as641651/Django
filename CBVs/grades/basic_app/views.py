from django.shortcuts import render
from basic_app import models
from basic_app import forms
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

class Index(TemplateView):
    template_name="index.html"

class UserFormView(FormView):
    form_class = forms.SiteUserForm
    #no need for fields when form_class is used (can also be used with CreateView)
    template_name = "basic_app/siteuser_form.html"
    success_url = reverse_lazy("index")

    def form_valid(self,form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        user.set_password(user.password)
        user.save()
        
        #create student form
        studentform = forms.StudentForm(self.request.POST)
        student = studentform.save(commit=False)
        student.candidate = user
        student.save()



        return super().form_valid(form)

def user_login(request):
    html_file = "basic_app/login.html"
    if request.method == 'POST':
        #Get the fields
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,html_file,{'status':'inactive'})
        else:
            print(username, " tried to login with password ", password)
            return render(request,html_file,{'status':'invalid'})
    else:
        return render(request,html_file,{'status':'success'})


@login_required
def user_logout(request):
    #The user is not logged out until this link is clicked
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class StudentsListView(ListView):
    model = models.Student
    context_object_name = 'student_list'

class StudentsSummaryView(DetailView):
    model = models.Student #Urls are linked only to IDs od Student. and not any other table

class UpdateStudentSummary(UpdateView):
    model = models.Student
    fields = ("grade","remark")

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        #has context 'student' and 'form'
        return context
