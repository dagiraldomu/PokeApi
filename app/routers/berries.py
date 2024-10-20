from fastapi import APIRouter, Depends, HTTPException
from app.schemas.berries import BerryGrowthStatistics
from app.services.berries import get_berries_from_cache_or_fetch
from app.services.histogram import html_content
from fastapi.responses import HTMLResponse
# Set up FastAPI router
router = APIRouter()


@router.get("/allBerryStats", response_model=BerryGrowthStatistics)
async def fetch_berries(data=Depends(get_berries_from_cache_or_fetch)):
    """
    Fetch all berries growth statistics from cache or external source(PokeApi endpoint).

    This endpoint returns a dict of berry statistics. The data is fetched either
    from a cache (if available) or from an external source.

    Returns:
        dict: A dictionary containing all berries growth statistics.
    """
    return data


@router.get("/berryStatsHistogram", response_class=HTMLResponse)
async def get_histogram(data=Depends(get_berries_from_cache_or_fetch)):
    """
    Generate a histogram of berry statistics and return as an HTML response.

    This endpoint generates a histogram based on the available berry growth statistics and returns
    it as an HTML page. If the data is not found, a 404 error is raised.

    Returns:
        HTMLResponse: An HTML page displaying the berry statistics histogram.

    Raises:
        HTTPException: If no berry data is found, a 404 error is returned.
        """
    if data:
        return HTMLResponse(content=html_content)
    else:
        raise HTTPException(status_code=404, detail="Berries data not found")