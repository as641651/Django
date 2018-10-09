from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    #Pass on the widget textarea. Otherwise, input looks same as that of name and email

    #Each field has certain default validation check.
    #We can also add custom Validation
    #Eg. Lets demonstrate botcather

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)
    ##Hidden input widget hides the field from rendering.
    ## But the field will be present in HTML element which a bot uses

    #Define a method starting with clean_<field_name>.
    #Django will automatically look for this method while Validation
    def clean_botcatcher(self):
        botcather = self.cleaned_data['botcatcher']
        if len(botcather):
            raise forms.ValidationError("Gotcha Bot!")
        return botcather

    ##Using django built-in validators
    botcather1 = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


    #Custom validator can also be passed in through validators arg
    #needs first argument to be 'value'
    def check_for_z(value):
        if value[0].lower() != 'z':
            raise forms.ValidationError("Needs to start with Z")

    refree = forms.CharField(validators=[check_for_z])

    verify_email = forms.EmailField(label="Re-enter email")

    ##We can also have a single validator for all fields at once
    def clean(self):
        #grab all clean data
        all_clean = super().clean()

        ##Prints only clean data
        print(super().clean())

        if 'email' in all_clean and 'verify_email' in all_clean:
            if all_clean['email'] != all_clean['verify_email']:
                raise forms.ValidationError("Make sure emails are same")


#Adding form input to model database

from app3.models import SignUp

class Form_SignUp(forms.ModelForm):
    #Can have validators/other modifications here. Not Compulsory.
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Name'}))
    #field name and form names should match
    class Meta:
        model = SignUp #Assign model
        fields = "__all__" # All fields in model
        #exclude = [exclude1,exclude2] #All model fields except
        #fields = (include1,include2) #Only these model fields
