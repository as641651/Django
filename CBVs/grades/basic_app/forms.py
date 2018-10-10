from django import forms
from . import models

class SiteUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.SiteUser
        fields = ('first_name','last_name','username','password','email')

class StudentForm(forms.ModelForm):
    # this line breaks the code when registering if required=False is not used
    remark = forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = models.Student
        #This line is important. skip candidate. otherwise form will fail to save under UserFormView
        fields = ('grade','remark')
