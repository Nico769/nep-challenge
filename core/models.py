from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

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


class Node(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    title = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="owned_nodes")

    class MPTTMeta:
        order_insertion_by = ["id"]


class Resource(UuidModel):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    owner = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="owned_resources")
    accessible_to = models.ManyToManyField(Role)
    container_node = models.ForeignKey(Node, null=True, on_delete=models.CASCADE, related_name="resources")
