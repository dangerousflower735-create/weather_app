"""Weather app: API key, weather data aur greeting functions."""

import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY_NAME = "OPENWEATHER_API_KEY"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def greet_user(name: str) -> str:
    """User ke naam ke sath welcome message return karta hai."""
    return f"Welcome, {name}!"


def weather_message(city: str, temperature_c: float) -> str:
    """Shehar aur temperature ka message banata hai."""
    return f"The temperature in {city} is {temperature_c} C."


def get_api_key() -> str:
    """Environment se OpenWeather API key leta hai."""
    key = os.getenv(WEATHER_API_KEY_NAME)
    if not key:
        raise ValueError(
            f"{WEATHER_API_KEY_NAME} file mein set nahi hai."
        )
    return key


def parse_weather_response(data: dict[str, Any]) -> tuple[str, float]:
    """API response se city aur Celsius temperature nikalta hai."""
    city = str(data["name"])
    temperature_c = float(data["main"]["temp"])
    return city, temperature_c


def get_weather(city: str) -> tuple[str, float]:
    """OpenWeather API se city ka current weather fetch karta hai."""
    response = requests.get(
        WEATHER_API_URL,
        params={
            "q": city,
            "appid": get_api_key(),
            "units": "metric",
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return parse_weather_response(data)


if __name__ == "__main__":
    print(greet_user("Shafaq"))

from datetime import datetime


PRAYER_API_URL = "https://api.aladhan.com/v1/timingsByCity"


def get_prayer_times(city: str, country: str = "Pakistan") -> dict[str, str]:
    """API se daily prayer timings fetch karta hai."""
    today = datetime.now().strftime("%d-%m-%Y")

    response = requests.get(
        f"{PRAYER_API_URL}/{today}",
        params={
            "city": city,
            "country": country,
            "method": 1,
        },
        timeout=10,
    )
    response.raise_for_status()

    result = response.json()
    timings = result["data"]["timings"]

    prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

    return {
        name: timings[name]
        for name in prayer_names
    }
