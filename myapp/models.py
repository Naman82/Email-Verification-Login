from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    dated=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.user.username
