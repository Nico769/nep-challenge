from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.model_abstracts import UuidModel


class Role(models.Model):
    class AvailableRoles(models.TextChoices):
        RESPONSABILE = "RESPONSABILE"
        OPERATORE = "OPERATORE"

    name = models.CharField(max_length=50, choices=AvailableRoles.choices)

    def __str__(self):
        return str(self.name)


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=Role.AvailableRoles.choices)


class Resource(UuidModel):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    owner = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="owned_resources")
    accessible_to = models.ManyToManyField(Role)
