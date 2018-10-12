from django.db import models
from django.urls import reverse

#Helps in passing strings as parameters to url
from django.utils.text import slugify
#helps in using markdown inside of the post
#pip install misaka
import misaka

from django.contrib.auth import get_user_model
#get model of the current user session
User = get_user_model()

from django import template
#USed to create custom template tags
register = template.Library()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)

    # A slug is a for something, containing only letters, numbers, underscores or hyphens (ie chars user in url).
    #allow_unicode : If True, the field accepts Unicode letters in addition to ASCII letters. Defaults to False.
    #ref: https://docs.djangoproject.com/en/2.1/ref/models/fields/
    slug = models.SlugField(allow_unicode=True,unique=True)

    description = models.TextField(blank=True,default='')
    #Used in case we want html version of our description
    #editable (option available for all fields):
    #If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.
    description_html =  models.TextField(editable=False,default='',blank=True)

    # Django will automatically generate a table to manage many-to-many relationships.
    # However, if you want to manually specify the intermediary table,
    # you can use the through option to specify the Django model that represents the intermediate table that you want to use.
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    #Funtion in models.Model that saves model to db
    def save(self,*args,**kwargs):
        #we set slug as the name(unique) of the group
        self.slug = slugify(self.name)
        #processes markdown
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        #path("posts/in/<slug>",views.SingleGroup.as_view(),name="single")
        return reverse('groups:single',kwargs={'slug':self.slug})

    #For list of model Meta options:
    # ref: https://docs.djangoproject.com/en/dev/ref/models/options/
    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='memberships')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_group')

    def __str__(self):
        return self.user.username

    class Meta:
        #Sets of field names that, taken together, must be unique:
        unique_together = ['group','user']
