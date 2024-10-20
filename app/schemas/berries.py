from pydantic import BaseModel
from typing import List, Dict

class BerryGrowthStatistics(BaseModel):
    berries_names: List[str]
    min_growth_time: str
    median_growth_time: str
    max_growth_time: str
    variance_growth_time: str
    mean_growth_time: str
    frequency_growth_time: Dict[int, int]

    class Config:
        json_schema_extra = {
            "example": {
                "berries_names": ["berry1", "berry2"],
                "min_growth_time": "10 hours",
                "median_growth_time": "12.5 hours",
                "max_growth_time": "20 hours",
                "variance_growth_time": "2.5 hours",
                "mean_growth_time": "15.0 hours",
                "frequency_growth_time": {"10": 2, "12": 3, "20": 1}
            }
        }
