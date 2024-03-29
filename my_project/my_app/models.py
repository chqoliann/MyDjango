from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DoctorTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()

class Patient(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='patients',
        related_query_name='patient',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='patients',
        related_query_name='patient',
    )
