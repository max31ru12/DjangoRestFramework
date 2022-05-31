from datetime import date, datetime
import uuid
from django.db import models
from users.models import User

class Project(models.Model):
    project_name = models.CharField(
        "project's name", 
        max_length=64, 
        default='NONAME project')

    repo_link = models.URLField(
        'repo link here', 
        default=uuid.uuid4)

    users_list = models.ManyToManyField("users.User") 

class ToDo(models.Model):
    project_name_todo = models.ForeignKey(Project, on_delete=models.CASCADE)

    note = models.CharField('note text', 
        max_length=128, 
        default='None note')
    
    date_created = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(default=datetime.now)
    note_creator = models.CharField('Creater username', max_length=128 ,default=User)




