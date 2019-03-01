from django import forms
from app3.models import SignUp

class SignUp_Form(forms.ModelForm):
    name = forms.CharField(label = "", widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}))
    email = forms.CharField(label= "", widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}))

    class Meta:
        model = SignUp
        fields = "__all__"
