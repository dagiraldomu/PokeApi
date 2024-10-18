import pytest
from httpx import AsyncClient, ASGITransport
from unittest import mock


mock.patch("fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f).start()

@pytest.fixture(scope="module")
async def client():
    from app.main import app # need to load app module after mock. otherwise, it would fail
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
