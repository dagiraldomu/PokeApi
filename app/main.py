import os
from fastapi import FastAPI
from app.routers import berries
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.settings.cache import init_cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the cache with in-memory backend
    await init_cache()
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
