from collections import defaultdict
import math
import httpx
from fastapi import Depends, HTTPException

from app.services.histogram import create_histogram
from app.settings.config import settings

from app.settings.cache import get_cache_backend
import numpy as np

import asyncio

async def fetch_berry_data(client, url):
    response = await client.get(url)
    berry = response.json()
    return {'name': berry['name'], 'growth_time': berry['growth_time']}


async def fetch_all_berries():
    url = settings.poke_api_berry_url

    async with httpx.AsyncClient() as client:
        while url:
            try:
                response = await client.get(url)
                data = response.json()

                results = data["results"]

                # Create tasks for all URLs
                tasks = [fetch_berry_data(client, result['url']) for result in results]

                # Run all tasks concurrently
                berries = await asyncio.gather(*tasks)

            except httpx.ConnectError as error:
                raise HTTPException(status_code=404, detail="Berries data endpoint unreachable")
            # Get the next page URL
            url = data['next']

        # Extract 'name' and 'growth_time' into two separate lists
        berries_names, growth_times = zip(*[(f'{berry["name"].title()} Berry', berry['growth_time']) for berry in berries])
        # Convert zip result to lists (zip returns tuples by default)
        berries_names = list(berries_names)
        growth_times = list(growth_times)

        # Create Histogram
        create_histogram(growth_times)

        # Convert growth_times to a numpy array
        growth_times_np = np.array(growth_times)

        # Calculate the statistics
        min_growth_time = np.min(growth_times_np)
        median_growth_time = np.median(growth_times_np)
        max_growth_time = np.max(growth_times_np)
        variance_growth_time = np.var(growth_times_np)  # Variance
        mean_growth_time = np.mean(growth_times_np)

        # Calculate the frequency of each growth time
        unique, counts = np.unique(growth_times_np, return_counts=True)
        frequency_growth_time = dict(zip(unique, counts))

        return {
            "berries_names": berries_names,
            "min_growth_time": f'{min_growth_time} hours',
            "median_growth_time": f'{round(median_growth_time, 2)} hours',
            "max_growth_time": f'{max_growth_time} hours',
            "variance_growth_time": f'{round(variance_growth_time, 2)} hours',
            "mean_growth_time": f'{round(mean_growth_time, 2)} hours',
            "frequency_growth_time": frequency_growth_time
        }

async def get_berries_from_cache_or_fetch(cache_backend=Depends(get_cache_backend)):
    # Look for cached response
    cached_value = await cache_backend.get('all_berry_records')
    if cached_value:
        return cached_value
    else:
        # Fetch all berry records asynchronously
        all_berry_records = await fetch_all_berries()
        await cache_backend.set('all_berry_records', all_berry_records, expire=settings.cache_expire_time)
        return all_berry_records