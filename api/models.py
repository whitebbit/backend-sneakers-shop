from typing import Any, Dict, Iterable, Optional, Tuple
from .utils.model_abstracts import Model
from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from . import receivers
from .utils import logging

class Size(Model):
    value = models.PositiveIntegerField(unique=True)

    def __str__(self) -> str:
        return str(self.value)

    def save(self, *args, **kwargs):
        cache.delete("size_cache")
        cache.delete("size_objects_cache")
        return super().save(*args, **kwargs)


class Sneaker(Model):
    name = models.CharField(max_length=200)
    article = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    sizes = models.ManyToManyField(Size)
    brand = models.CharField(max_length=200)

    caced_sneakers = set()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        cache.delete("sneakers_cache")
        return super().save(*args, **kwargs)


post_delete.connect(receivers.delete_sneaker_cache, sender=Sneaker)
post_delete.connect(receivers.delete_size_cache, sender=Size)
post_save.connect(receivers.delete_sneaker_cache, sender=Sneaker)
post_save.connect(receivers.delete_size_cache, sender=Size)