from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache import FastAPICache

cache_backend = None

async def init_cache():
    global cache_backend
    cache_backend = InMemoryBackend()
    FastAPICache.init(cache_backend, prefix="fastapi-cache")

def get_cache_backend():
    return cache_backend
