from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class POST(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)