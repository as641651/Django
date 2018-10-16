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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.kwargs)
    #     return context

from django.shortcuts import get_object_or_404
from django.contrib import messages

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    #We have to get a specific Group object and create a new GroupMember

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning! Already a member')
        else:
            messages.success(self.request,'You are now a member!')

        return super().get(request,*args,**kwargs)

    def get_redirect_url(self,*args,**kwargs):
        return reverse("groups:single",kwargs={'slug':self.kwargs.get('slug')})

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry You are not in this group')
        else:
            membership.delete()
            messages.success(self.request,'You are not a member anymore!')

        return super().get(request,*args,**kwargs)

    def get_redirect_url(self,*args,**kwargs):
        return reverse("groups:single",kwargs={'slug':self.kwargs.get('slug')})
