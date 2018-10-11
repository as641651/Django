from django import forms
from blog import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('author','title','text')

        #modifying html attributes of fields in views.py
        #This can also be done via template filters
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            #editable and medium editor comes from medium library
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('author','text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
