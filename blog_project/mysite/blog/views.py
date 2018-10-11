from django.shortcuts import render
from blog import models
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                DetailView,CreateView,
                                UpdateView, DeleteView)

# Create your views here.
#about/
#about.html
class AboutView(TemplateView):
    template_name="blog/about.html"

#Home page
#post_list.html
class PostListView(ListView):
    model = models.Post

    #method to grab the list and order them
    def get_queryset(self):
        # __lte implies less than or equal to
        #grab all posts less than current time and order by date in decending order (-published_date)
        return models.Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
        #translates to SQL Command
        # SELECT * FROM Post WHERE pub_date <= '2006-01-01';
        #google django db queries field lookup to see the list of comparisions available

#post/<pk>
#post_detail.html
class PostDetailView(DetailView):
    model = models.Post

#We use this instead of Decoratoer @login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog import forms

#post/new/
#post_form.html
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.PostForm
    model = models.Post

#post/<pk>/edit
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.PostForm
    model = models.Post

from django.urls import reverse_lazy

#post/<pk>/remove
#post_confirm_delete.html
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Post
    success_url = reverse_lazy('post_list')

#drafts/
#post_draft_list.html
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = models.Post
    template_name = 'blog/post_draft_list.html'

    #Get list of unpublished posts
    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull=True).order_by('create_date')

###############################
##############################

from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

#post/<int:pk>/comment/
#comment_form.html
# @login_required
def add_comment_to_post(request,pk):
    #pk of post
    post = get_object_or_404(models.Post,pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail',pk=post.pk)
    else:
        form = forms.CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})

#comment/<pk>/approve
@login_required
def comment_approve(request,pk):
    #pk of comment
    comment = get_object_or_404(models.Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

#comment/<pk>/approve
@login_required
def comments_remove(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

#post/<pk>/publish
@login_required
def post_publish(request,pk):
    post = get_object_or_404(models.Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
