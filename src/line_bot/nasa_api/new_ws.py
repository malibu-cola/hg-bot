import os
from datetime import date, timedelta
import requests
from textwrap import dedent


def fetch_new_ws() -> str | None:
    nasa_key = os.getenv("NASA_API_KEY")
    url = "https://api.nasa.gov/neo/rest/v1/feed"

    # 日付設定（直近3日分）
    start_date = date.today() - timedelta(days=0)
    end_date = date.today()

    params = {
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "api_key": nasa_key,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 最初の天体を表示
    ret = ""
    near_earth_objects = data["near_earth_objects"]
    for date_key in sorted(near_earth_objects.keys())[:3]:
        for obj in near_earth_objects[date_key]:
            is_hazard = bool(obj["is_potentially_hazardous_asteroid"])
            if is_hazard:
                ret += dedent(f"""
                📅 日付:", {date_key}
                🪨 名称:", {obj["name"]}
                📏 直径推定値: 
                    {round(obj["estimated_diameter"]["meters"]["estimated_diameter_min"], 2)}[m]~{round(obj["estimated_diameter"]["meters"]["estimated_diameter_max"], 2)}[m]
                🚀 地球からの相対速度 (km/h): 
                    {round(float(obj["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]), 2)}
                🌍 最接近時の距離(km):
                    {round(float(obj["close_approach_data"][0]["miss_distance"]["kilometers"]), 2)}
                🧨 危険かどうか: {obj["is_potentially_hazardous_asteroid"]}
                {"-" * 40}""")
    return ret[:4900] if ret else None
