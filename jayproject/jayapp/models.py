from django.db import models
from datetime import datetime

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    #user_id=models.AutoField(primary_key=True)

class TodoListItem(models.Model):
    id=models.AutoField(primary_key=True)
    content=models.TextField()
    status=models.BooleanField(default=False)
    user_email=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    date_completed=models.DateTimeField(auto_now_add=True)