from datetime import timezone

from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=3)
    mail_addr = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def login_at(self):
        self.updated_at = timezone.now()
        self.save()
