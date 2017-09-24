"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from userprofile import views as profileview
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^userprofile/?$',profileview.profile,name="userprofile"),
    url(r'^login/?$',views.login_view,name="login"),

    url(r'^authencite_user_login=only/?$',views.logedin_view,name="login_auth"),
    url(r'^authencite_user_logout=only/?$',views.logout_view,name="logout_auth"),
    url(r'^authencite_user_postcreate=only/?$', views.postcreate, name="post_auth"),
    url(r'^authencite_user_postreade=only/?$', views.postread_view, name="postread_auth"),
    url(r'^authencite_user_postcomment=only/(?P<slug>[-\w]+)$',views.postcomments,name='post_comments'),
    url(r'^authencite_user_postonlymodify=only/?$', views.postmodify_view, name="postmodify_auth"),
    url(r'^authencite_user_updateparticularpost=only/(?P<name>\d+)/$', views.postupdate_view, name="postupdate_auth"),
    url(r'^authencite_user_updateparticularpost=only/(?P<name>\d+)/modified/$', views.modified_view, name="postmodified_auth"),
    url(r'^authencite_user_updateparticularpost=only/(?P<name>\d+)/delete/$', views.delete_view,name="postdelete_auth"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









''' url('^', include('django.contrib.auth.urls')),
    these url will be included
    ^login/$ [name='login']
    ^logout/$ [name='logout']
    ^password_change/$ [name='password_change']
    ^password_change/done/$ [name='password_change_done']
    ^password_reset/$ [name='password_reset']
    ^password_reset/done/$ [name='password_reset_done']
    ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    ^reset/done/$ [name='password_reset_complete']'''