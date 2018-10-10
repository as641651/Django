from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256,unique=True)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name #This is printed when used as Foreign key

    #This needs to be implemented to use CreateView
    def get_absolute_url(self):
        return reverse("details",kwargs={'pk':self.pk})
        # return "/listview/"

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    #the use of related name can be seen in list view
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name
