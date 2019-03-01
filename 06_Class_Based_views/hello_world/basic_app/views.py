from django.shortcuts import render

# Create your views here.
# def index(request):
    # return render(request,'index.html')

#Simple class based view
from django.views.generic import View

class CBView(View):
    def get(self,request):
        #contents as under index(request)
        return render(request,'index.html',{'text':'Simple CBV'})


#Template view
from django.views.generic import TemplateView

class IndexView(TemplateView):

    template_name = 'index.html'

    #Injecting content
    def get_context_data(self,**kwargs):
        # **kwargs are the other key word args
        context = super().get_context_data(**kwargs)
        context['text'] = "Template view!"
        return context


#List view
from django.views.generic import ListView
from . import models

#Lists all the school
class SchoolListView(ListView):
    model = models.School
    #This class takes in the model class name, lower cases it and creates default context object and html files

    template_name = 'index.html'
    # in absense of template_name, this class will look into 'basic_app/school_list.html'

    context_object_name = 'schools'
    # in absence of context name, it will be 'school_list'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "List view!"
        return context

#Detail view
from django.views.generic import DetailView

#Lists the details of school, like students
#Each entery in the model gets a separate URL
class SchoolDetailView(DetailView):
    model = models.School

    template_name = 'index.html'
    # in absense of template_name, this class will look into 'basic_app/school_detail.html'

    context_object_name = 'school_detail'
    # in absence of context name, it will be 'school'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Detail view!"
        return context

#CreateView
from django.views.generic import CreateView
#Creates a form to add entry into model
class SchoolCreateView(CreateView):
    model = models.School
    #fields are mandatory
    fields = ('name','principal','location')
    template_name = 'index.html'
    #by default, looks for basic_app/school_form.html
    # context variable = form

#UpdateView
from django.views.generic import UpdateView

#Each entry gets a separate URL
class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')
    # if {{form.location}} is used in html, it wont be rendered

    template_name= 'index.html'
    #by default, looks for basic_app/school_form.html
    # context variable = form

#DeleteView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

#Each entry gets a separate URL
class SchoolDeleteView(DeleteView):
    model = models.School
    #reverse_lazy redirects only upon success
    success_url = reverse_lazy("list")
    template_name= 'school_confirm_delete.html'
    #basic_app/school_confirm_delete.html is the default html file
    context_object_name = 'school_delete'
    #default is school
