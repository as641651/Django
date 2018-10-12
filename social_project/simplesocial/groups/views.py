from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from groups.models import Group, GroupMember

# Create your views here.

#groups/new
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group
    template_name = "groups/group_form.html"
    #Using reverse instead of reverse_lazy breaks compilation with circular import error
    #success url overrides get_absolute_url defined in Models
    #success_url = reverse_lazy("index")

#/groups/posts/in/<slug>
class SingleGroup(generic.DetailView):
    model = Group
    template_name = "groups/group_detail.html"

#groups/
class ListGroups(generic.ListView):
    model = Group
    template_name = "group_list.html"
