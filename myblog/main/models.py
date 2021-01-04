from django.db import models
from datetime import datetime
# from markdownx.models import MarkdownxField
# from markdownx.utils import markdownify
# Create your models here.
# Create your models here.class BlogPost(models.Model):    # id - Django automatically creates an auto-incrementing primary key  

class BlogPost(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)    
    subtitle = models.CharField(max_length=180, null=True, blank=False)    
    slug = models.CharField(max_length=240, null=True, blank=False) 
    photo = models.ImageField(default='default.png',blank=True,upload_to=datetime.now().strftime('django-summernote/%Y-%m'))   
    body = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True, null=False)    
    updated_at = models.DateTimeField(auto_now=True, null=False)
    # body = MarkdownxField()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Blog : {} , published on: {}'.format(self.title, self.created_at)

    # @property
    # def formatted_markdown(self):
        # return markdownify(self.body)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)