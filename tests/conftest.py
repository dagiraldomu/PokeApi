import pytest
from httpx import AsyncClient, ASGITransport
from unittest import mock


# Mock function for get_berries_from_cache_or_fetch
def mock_get_berries_from_cache_or_fetch():
    return {
        "berries_names": ["berry1", "berry2"],
        "min_growth_time": "10 hours",
        "median_growth_time": "12.5 hours",
        "max_growth_time": "20 hours",
        "variance_growth_time": "2.5 hours",
        "mean_growth_time": "15.0 hours",
        "frequency_growth_time": {"10": 2, "12": 3, "20": 1}
    }


mock.patch("app.services.berries.get_berries_from_cache_or_fetch", mock_get_berries_from_cache_or_fetch).start()
