from fastapi import FastAPI
from app.routers import berries
import os

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the cache with in-memory backend
    print('cache running')
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    yield

app = FastAPI(title="PokeApi", description="Berries statistics", lifespan=lifespan)

app.include_router(berries.router)



if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
