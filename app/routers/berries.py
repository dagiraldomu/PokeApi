from fastapi import APIRouter
from fastapi_cache.decorator import cache
from app.services.berries import fetch_all_berries
from app.services.histogram import html_content
from app.settings.config import settings
from fastapi.responses import HTMLResponse
# Set up FastAPI router
router = APIRouter()


@router.get("/allBerryStats")
@cache(expire=settings.cache_expire_time)
async def fetch_berries():
    # Fetch all berry records asynchronously
    all_berry_records = await fetch_all_berries()

    # Limit the response to the specified number of records
    return all_berry_records

@router.get("/BerryStatsHistogram", response_class=HTMLResponse)
async def get_histogram():
    return HTMLResponse(content=html_content)