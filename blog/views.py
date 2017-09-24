from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from .forms import signinform,loginform,postform,postmodifyform,commentform
from django.shortcuts import render,redirect,get_object_or_404
from .models import sighinmodel,postmodel,commentmodel
from django.contrib import messages
from django import forms
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from userprofile import models
from django.conf import settings


def home(request):
    form=signinform(request.POST or None)
    title="Sign in"
    if request.POST:
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/authencite_user_login=only/")

    return render(request ,"home.html", {"form": form, "title": title})


def login_view(request):
    form=loginform(request.POST or None)
    title="Login"
    if request.POST:
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            fullname= form.cleaned_data["fullname"]
            #print (email)
            #send_mail('Subject here', 'Here is the message.',settings.EMAIL_HOST_USER, [email], fail_silently=False)
            instance = User.objects.create_user(username=username,password=password,email=email)
            instance2=sighinmodel(id=None,fullname=fullname,relateduser=instance)
            instance2.save()
            login(request, instance)
            return redirect("/authencite_user_login=only/")
    return render(request,"login.html",{"form":form ,"title":title})


@login_required
def logedin_view(request):
    title1 = "view post"
    instance = postmodel.objects.order_by('-updated')
    return render(request, "postread.html", {"instance":instance,"title": title1})


@login_required
def logout_view(request):
    title = "Loged out"
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def postcreate(request):
    title1 = "create post"
    if request.POST:
        form = postform(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            subject=form.cleaned_data["subject"]
            instance = postmodel.objects.create(title=title,body=body,subject=subject,author=request.user)
            instance.save()
    form = postform()
    return render(request, "postcreate.html", {"form":form,"title": title1})

@login_required
def postread_view(request):
    title1 = "view post"
    if request.POST:
        return HttpResponse("no post request on this page")

    instance = postmodel.objects.order_by('-updated')
    paginator = Paginator(instance, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        instance = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        instance = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        instance = paginator.page(paginator.num_pages)

    return render(request, "postread.html", {"instance":instance,"title": title1})

@login_required
def postcomments(request,slug):
    title1 = "comment"
    if request.POST:
        form = commentform(request.POST)
        if form.is_valid():
            post = get_object_or_404(postmodel,slug=slug)
            comment = form.cleaned_data["comment"]
            instance = commentmodel.objects.create(commentauthor=request.user, commentpost=post, comments=comment)
            instance.save()
            return redirect(request.path)
    form = commentform()
    post = get_object_or_404(postmodel, slug=slug)
    commentinstance = commentmodel.objects.filter(commentpost=post).order_by("-commenttime")
    return render(request,"postcomment.html",{"title":title1,"form":form,"post":post,"comment":commentinstance})


@login_required
def postmodify_view(request):
    title1 = "view post"
    instance = postmodel.objects.filter(author=request.user)
    instance = instance.order_by('-updated')
    return render(request, "userpost.html", {"instance":instance,"title": title1})

@login_required
def postupdate_view(request,name=None):
    title1="moodify your post"
    if request.POST:
        instance=get_object_or_404(postmodel,id=name)
        form = postmodifyform(initial={"title":instance.title,"body":instance.body,"subject":instance.subject})
        return render(request, "modify.html", {"name":name,"form":form,"instance":instance,"title":title1})
    return HttpResponse(name)

@login_required
def modified_view(request,name):
    if request.POST:
        form = postmodifyform(request.POST or None)
        if form.is_valid():
            instance = get_object_or_404(postmodel, id=name)
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            subject=form.cleaned_data["subject"]
            instance.title=title
            instance.body=body
            instance.subject=subject
            instance.save()
            title1 = "view post"
            instance = postmodel.objects.order_by('-updated')
            return render(request, "postread.html", {"instance":instance,"title": title1})

@login_required
def delete_view(request,name):
    if request.POST:
        get_object_or_404(postmodel, id=name).delete()
        return HttpResponseRedirect("/authencite_user_postreade=only/")


