from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Table des clients
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Client"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Table de status de tâche
class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


# Table des tâches
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)
    note = models.TextField(max_length=1000, blank=True)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tâche"
        ordering = ["-startDate"]

    def __str__(self):
        return self.customer.name + " | " + self.title

    def get_absolute_url(self):
        return reverse("update_task", kwargs={"pk": self.pk})


# Table des rendez-vous
class Schedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(blank=True, null=True)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Planning"

    def __str__(self):
        return self.title




