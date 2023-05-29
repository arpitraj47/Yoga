from django.db import models

# Create your models here.

class user_information(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.IntegerField()

