from collections import defaultdict
import math
import httpx
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

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

                berries_names.append(f'{name.title()} Berry')
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

        variance_growth_time = sum_squared_diff / (count - 1) if count > 1 else 0.0 # TODO Change to numpy?

        # Calculate median (needs sorting, unavoidable but only done once)
        growth_times.sort()
        mid = count // 2
        if count % 2 == 0:
            median_growth_time = (growth_times[mid - 1] + growth_times[mid]) / 2
        else:
            median_growth_time = growth_times[mid]

        return {
            "berries_names": berries_names,
            "min_growth_time": f'{min_growth_time} hours',
            "median_growth_time": f'{round(median_growth_time, 2)} hours',
            "max_growth_time": f'{max_growth_time} hours',
            "variance_growth_time": f'{round(variance_growth_time, 2)} hours',
            "mean_growth_time": f'{round(mean_growth_time, 2)} hours' ,
            "frequency_growth_time": dict(frequency_growth_time)
        }