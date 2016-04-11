from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    
    
class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'post')
    content = models.CharField(max_length = 100)
    postTime = models.DateTimeField(auto_now_add = True)
    
    
class SharedReference(models.Model):
    user = models.ForeignKey(User, related_name = 'sharedPost')
    content = models.CharField(max_length = 100)
    postTime = models.DateTimeField(auto_now_add = True)
    referedPost = models.ForeignKey(Post)
    
    
class SharedNode(models.Model):
    level = models.IntegerField(default = -1)
    next = models.ForeignKey('self')