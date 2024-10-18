import os
import httpx
from fastapi import APIRouter
from dotenv import load_dotenv


from collections import defaultdict
from typing import List, Dict
import math

import matplotlib.pyplot as plt
import numpy as np


from fastapi_cache.decorator import cache



# Load environment variables from .env file
load_dotenv()

# Set up FastAPI router
router = APIRouter()

# Fetch API URL from environment variables (from .env file)
API_BASE_URL = os.getenv("POKEAPI_BERRY_URL", "https://pokeapi.co/api/v2/berry/")

async def fetch_all_berries():
    url = API_BASE_URL
    # all_berries = []
    berries_names = []
    growth_times = []

    # Initialize variables for the statistics
    min_growth_time = math.inf
    max_growth_time = -math.inf
    sum_growth_time = 0
    sum_squared_diff = 0  # For calculating variance
    frequency_growth_time = defaultdict(int)

    async with httpx.AsyncClient() as client:
        while url:
            response = await client.get(url)
            data = response.json()

            results = data["results"]

            for result in results:
                response_berry_data = await client.get(result['url'])
                berry = response_berry_data.json()

                name = berry['name']
                growth_time = berry['growth_time']

                berries_names.append(name)
                growth_times.append(growth_time)

                # Update min, max, sum
                min_growth_time = min(min_growth_time, growth_time)
                max_growth_time = max(max_growth_time, growth_time)
                sum_growth_time += growth_time

                # Update frequency
                frequency_growth_time[growth_time] += 1



            # Get the next page URL
            url = data['next']

        # Calculate mean
        count = len(growth_times)
        mean_growth_time = sum_growth_time / count if count > 0 else 0

        # Calculate variance
        for growth_time in growth_times:
            sum_squared_diff += (growth_time - mean_growth_time) ** 2

        variance_growth_time = sum_squared_diff / (count - 1) if count > 1 else 0.0

        # Calculate median (needs sorting, unavoidable but only done once)
        growth_times.sort()
        mid = count // 2
        if count % 2 == 0:
            median_growth_time = (growth_times[mid - 1] + growth_times[mid]) / 2
        else:
            median_growth_time = growth_times[mid]

        return {
            "berries_names": berries_names,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": dict(frequency_growth_time)
        }

@router.get("/allBerryStats")
@cache(expire=60)
async def fetch_berries():
    # Fetch all berry records asynchronously
    all_berry_records = await fetch_all_berries()

    # Limit the response to the specified number of records
    return all_berry_records

