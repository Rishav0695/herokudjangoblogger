from django.contrib import admin

# Register your models here.
from .models import userprofile
from django.contrib.auth.models import User
class userprofileAdmin(admin.ModelAdmin):

    list_display=["__str__","user","profileimage","admin_image"]
    class meta:
        model=userprofile
admin.site.register(userprofile,userprofileAdmin)