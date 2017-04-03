from django.db import models

# Create your models here.


class User(models.Model):
    userID = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Job(models.Model):
    jobID = models.IntegerField(primary_key=True, auto_created=True)
    creatorUserID = models.IntegerField()
    workerUserID = models.IntegerField()
    category = models.CharField(max_length=25)
    compensation = models.IntegerField()
    description = models.CharField(max_length=200)



