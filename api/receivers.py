from django.core.cache import cache
from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete, sender=None)
def delete_sneaker_cache(*args, **kwargs):
    cache.delete("sneaker_cache")

@receiver(post_delete, sender=None)
def delete_size_cache(*args, **kwargs):
    cache.delete("size_cache")
    cache.delete("size_objects_cache")
