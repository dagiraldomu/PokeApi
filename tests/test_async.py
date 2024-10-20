import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_fetch_berry_stats():

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/allBerryStats")

    assert response.status_code == 200
    # Check if the 'Content-Type' header is 'application/json'
    assert response.headers["content-type"] == "application/json"
    # Validate the response data matches the mock
    expected_data = {
        "berries_names": ["berry1", "berry2"],
        "min_growth_time": "10 hours",
        "median_growth_time": "12.5 hours",
        "max_growth_time": "20 hours",
        "variance_growth_time": "2.5 hours",
        "mean_growth_time": "15.0 hours",
        "frequency_growth_time": {"10": 2, "12": 3, "20": 1}
    }

    assert response.json() == expected_data

@pytest.mark.asyncio
async def test_histogram_berry_stats():

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/berryStatsHistogram")

    assert response.status_code == 200
    # Check if the 'Content-Type' header is 'text/hml'
    assert response.headers["content-type"] == "text/html; charset=utf-8"
