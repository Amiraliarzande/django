from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=255)
    content= models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    counted_viwe= models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "{} - {}".format(self.id, self.title)
    
    def get_absolute_url(self):
        return reverse("blog:blog_single", kwargs={"pid": self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
