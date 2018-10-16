from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
#pip install django-braces
from braces.views import SelectRelatedMixin
from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

from groups.models import Group

# Create your views here.
#posts/
class PostList(generic.ListView):
    model = models.Post
    # select_related = ('user','group')
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups_of_user"] = []
        if self.request.user.is_authenticated:
            context["groups_of_user"] = Group.objects.filter(members__in=[self.request.user])
        return context

#by/<username>
class UserPost(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            #get the user object from db matching certain criteria. Recall it was difficult to get object attributes of another class inside CBVs.
            #This is how it is done
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            #executed when there is exception
            raise Http404
        else:
            #this statement will be executed when there is no exception
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        print(self.kwargs)
        return context

#by/<username>
class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        #filter Post based on username
        #This is needed may be because we use something else other than pk for reference
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))

#posts/new
class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ("message","group")
    model = models.Post
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

from django.contrib import messages

#delete/<pk>
class DeletePost(LoginRequiredMixin,SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
