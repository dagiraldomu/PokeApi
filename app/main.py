from fastapi import FastAPI
from app.routers import berries
import os
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the cache with in-memory backend
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    yield

app = FastAPI(title="PokeApi", description="Berries statistics", lifespan=lifespan)

app.include_router(berries.router)

# Serve the 'static' directory for images
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
