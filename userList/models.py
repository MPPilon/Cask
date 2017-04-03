from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)


class Job(models.Model):
    creatorUser = models.ForeignKey(User, related_name='creator')
    workerUser = models.ForeignKey(User, related_name='worker')
    category = models.CharField(max_length=25)
    compensation = models.IntegerField()
    description = models.CharField(max_length=200)
    photo = models.CharField(max_length=11)
