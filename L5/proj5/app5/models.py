from django.db import models
#Import User from authorization models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    #Has-a relationship with User class!
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Attributes under User :

    # username
    # password
    # email
    # first_name
    # last_name


    #additional attributes
    portfolio_site = models.URLField(blank=True)
    #upload_to='profile_pics' requires profile_pics to be a sub-dir under media
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
