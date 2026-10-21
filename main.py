"""Weather app ka main module: API key padhta hai aur greeting/weather message banata hai."""

import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY_NAME = "OPENWEATHER_API_KEY"


def greet_user(name: str) -> str:
    """User ke naam ke sath welcome message return karta hai."""
    return f"Welcome, {name}!"


def weather_message(city: str, temperature_c: float) -> str:
    """Shehar aur temperature ke sath weather message return karta hai."""
    return f"The temperature in {city} is {temperature_c} C."


def get_api_key() -> str:
    """.env se API key padhta hai. Agar key na mile to error deta hai."""
    key = os.getenv(WEATHER_API_KEY_NAME)
    if not key:
        raise ValueError(
            f"{WEATHER_API_KEY_NAME} .env file mein nahi mili. .env check karein."
        )
    return key
