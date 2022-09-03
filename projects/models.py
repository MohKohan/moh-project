from django.db import models
import uuid
from users.models import Profile

class Tag(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    owner=models.ForeignKey(Profile,blank=True,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    project_image=models.ImageField(blank=True,null=True,default="default.jpg")
    used_links=models.CharField(max_length=900,blank=True,null=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Create your models here.
