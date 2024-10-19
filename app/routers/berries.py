from fastapi import APIRouter, Depends
from app.settings.cache import get_cache_backend
# from fastapi_cache.decorator import cache
from app.services.berries import fetch_all_berries
from app.services.histogram import html_content
from app.settings.config import settings
from fastapi.responses import HTMLResponse
# Set up FastAPI router
router = APIRouter()


@router.get("/allBerryStats")
async def fetch_berries(cache_backend=Depends(get_cache_backend)):
    # Look for cached response
    cached_value = await cache_backend.get('all_berry_records')
    if cached_value:
        return cached_value
    else:
        # Fetch all berry records asynchronously
        all_berry_records = await fetch_all_berries()
        await cache_backend.set('all_berry_records', all_berry_records, expire=settings.cache_expire_time)
        return all_berry_records

@router.get("/BerryStatsHistogram", response_class=HTMLResponse)
async def get_histogram():
    return HTMLResponse(content=html_content)