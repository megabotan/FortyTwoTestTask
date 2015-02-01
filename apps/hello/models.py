from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    other_contacts = models.TextField()

class Request(models.Model):
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)