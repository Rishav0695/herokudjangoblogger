from django.contrib import admin
from .forms import signinform
from .models import sighinmodel,postmodel,commentmodel
from django.contrib.auth.models import User
class SignUpAdmin(admin.ModelAdmin):
    list_display=["__str__"]
    class meta:
        model=sighinmodel
admin.site.register(sighinmodel,SignUpAdmin)
class postAdmin(admin.ModelAdmin):
    list_display = ["__str__","author","updated","timestamp","id"]
    class meta:
        model=postmodel
admin.site.register(postmodel,postAdmin)
class commentAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class meta:
        model = commentmodel
admin.site.register(commentmodel,commentAdmin)