from enum import Enum
from django.db import models

class Roles(models.IntegerChoices):
    ADMIN = 1
    PARTICIPANT = 2
    TEAMLEADER = 3
    JUDGE = 4

class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    role = models.IntegerField(choices=Roles.choices, default=Roles.PARTICIPANT)

    def __str__(self):
        return self.userName
    