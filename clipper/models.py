from django.db import models

from django.contrib.auth.models import User

class UserClipboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clipboard_id = models.CharField(max_length=32)
