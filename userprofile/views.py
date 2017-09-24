
from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django import forms
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import userprofileform
from .models import userprofile
import os
from blog import models
from blogger import settings


def profile(request):
    if request.method=='POST':
        form = userprofileform(request.POST or None, request.FILES or None)
        if form.is_valid():
            profileimage = form.cleaned_data["profileimage"]
            ins = userprofile.objects.filter(user=request.user)
            for i in ins:
                i.delete()
            instance = userprofile.objects.create(user=request.user,profileimage=profileimage)
            instance.save()
    instance2 = models.sighinmodel.objects.filter(relateduser=request.user)
    instance1 = userprofile.objects.filter(user=request.user)
    form = userprofileform(request.GET or None)

    return render(request,"userprofile.html",{"form":form,"instance":instance1,"instance2":instance2})
