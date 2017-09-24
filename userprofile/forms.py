from django import forms
from .models import userprofile
from django.core import validators
from django.contrib.auth.models import User

class userprofileform(forms.Form):
    profileimage = forms.ImageField()
    class Meta:
        fields = ['profileimage']

