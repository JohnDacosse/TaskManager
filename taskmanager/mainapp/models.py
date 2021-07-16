from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Table des utilisateurs
#class Users(models.Model):
#    username = models.CharField(max_length=200)
#    password = models.CharField(max_length=200)

#    def __str__(self):
#        return self.username

# Table des clients
class Clients(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Table de status de tâche
class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


# Table des tâches
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)
    note = models.CharField(max_length=1000, blank=True)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name + " | " + self.title


# Table des rendez-vous
class Schedules(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(blank=True, null=True)
    user = models.ManyToManyField(User)




