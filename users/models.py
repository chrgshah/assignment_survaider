from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    employment_type = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    race = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'users'