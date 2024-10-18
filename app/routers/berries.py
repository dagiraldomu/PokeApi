from fastapi import APIRouter
from fastapi_cache.decorator import cache
from app.services.berries import fetch_all_berries

# Set up FastAPI router
router = APIRouter()


@router.get("/allBerryStats")
@cache(expire=60)
async def fetch_berries():
    # Fetch all berry records asynchronously
    all_berry_records = await fetch_all_berries()

    # Limit the response to the specified number of records
    return all_berry_records

