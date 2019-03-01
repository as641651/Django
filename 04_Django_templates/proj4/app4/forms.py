from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='', max_length=100)
