from django.db import models

from django.contrib.auth.models import User


class Thought(models.Model):
    
    title =  models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    date_posted = models.DateField(auto_now_add=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


class Profile(models.Model):
    
    profile_picture = models.ImageField(blank=True,null=True,default='default/default.png')
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
