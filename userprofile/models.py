
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, related_name='userprofile',on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)
    description = models.TextField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)