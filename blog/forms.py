from django import forms
from .models import sighinmodel,postmodel,commentmodel
from django.core import validators
from django.contrib.auth.models import User


class signinform(forms.Form):
    username= forms.CharField(max_length=None)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields=["username","password"]

    def clean_username(self):
        username = self.cleaned_data['username']#cleaned_data gives the data in the form of text.
        if User.objects.filter(username=username).exists():#if user name exists
            return username
        else:
            raise forms.ValidationError(u'Username "%s" does not exists.' % username)
        return username


class loginform(forms.Form):
    CHOICE=(("male","male"),("female","female"))
    fullname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=None)
    email = forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =["email","username","password","password_confirm","fullname"]

    def clean(self):
        password1=self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')
        if password1 != password2:
            raise forms.ValidationError({"password":"field not match"})

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username


class postform(forms.ModelForm):
    title = forms.CharField(max_length=None)
    body = forms.Textarea()
    subject=forms.Textarea()

    class Meta:
        model = postmodel

        fields =["title","subject","body"]

class postmodifyform(forms.Form):

    title = forms.CharField(max_length=None,widget=forms.Textarea(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    subject=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control '}))

    class Meta:
        fields=["title","subject","body"]

class commentform(forms.ModelForm):
    comment = forms.CharField(max_length=None)
    class Meta:
        model = commentmodel
        fields = ["comment"]
