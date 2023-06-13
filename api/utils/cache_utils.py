from django.core.cache import cache

debug = False


def make_cache(cache_name, cache_data, cache_time=60):
    current_cache = cache.get(cache_name)
    if current_cache:
        if debug:
            print(f"{cache_name} cache")
        return current_cache
    else:
        if debug:
            print(f"{cache_name} not cache")
        cache.set(cache_name, cache_data, cache_time)
        return cache_data
