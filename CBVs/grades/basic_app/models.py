from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class SiteUser(User):
    def get_absolute_url(self):
        return "/"

class StudentMarks(models.Model):
    #default value/null is needed if a field is added after migration.
    #Otherwise migrations may have to be restarted by deleting the db and migration files
    candidate = models.OneToOneField(SiteUser,on_delete=models.CASCADE,null=True)
    maths = models.PositiveIntegerField(blank=True,null=True)
    science = models.PositiveIntegerField(blank=True,null=True)
    english = models.PositiveIntegerField(blank=True,null=True)
    tamil = models.PositiveIntegerField(blank=True,null=True)
    evs = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name

    def get_absolute_url(self):
        #Dirty trick. Users Pk is not equal to Students pk. cuz of Superusers
        return reverse("app:details",kwargs={'pk':self.candidate.pk-1})

class Student(models.Model):
    candidate = models.OneToOneField(SiteUser,on_delete=models.CASCADE)
    grade = models.CharField(max_length=1,blank=True)
    #remark should be TextField to appear as text widget
    remark = models.CharField(max_length=256,blank=True)
    marks = models.OneToOneField(StudentMarks,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name

    def get_absolute_url(self):
        return reverse("app:details",kwargs={'pk':self.pk})
