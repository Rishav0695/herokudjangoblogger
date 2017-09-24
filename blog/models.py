from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class sighinmodel(models.Model):
    relateduser = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    fullname = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.fullname

class postmodel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,default=None)
    body=models.TextField()
    slug = models.SlugField(unique=True)
    subject=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_dpetail', (),
                {
                    'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        super(postmodel, self).save(*args, **kwargs)
        if not self.slug:

            self.slug = slugify(self.title)+"-"+str(self.id)
            self.save()

    def __str__(self):
        return self.title
        #return '%s %s' %(self.title,self.author)


class commentmodel(models.Model):
    commentauthor = models.ForeignKey(User,default=None)
    commentpost= models.ForeignKey(postmodel,default=None)
    comments = models.TextField(default="")
    commenttime = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.comments

