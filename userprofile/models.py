from django.db import models
from django.contrib.auth.models import User
import os
from blogger import settings

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to="userprofile/")
    class meta:
        database ="profileimage"
    def admin_image(self):
        return '<img src="%s" width=40 height=40/>' % self.profileimage.url

    def delete(self, *args, **kwargs):
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.profileimage.name))
            super(userprofile, self).delete(*args, **kwargs)
        except OSError:
            pass

    admin_image.allow_tags = True