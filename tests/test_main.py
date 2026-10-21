"""Tests for the weather app's main module."""

import pytest
from main import get_api_key, greet_user, weather_message


def test_greet_user_returns_welcome_message() -> None:
    """greet_user should return a welcome line with the name."""
    assert greet_user("Shafaq") == "Welcome, Shafaq!"


def test_weather_message_formats_temperature() -> None:
    """weather_message should show city and temperature in one line."""
    assert weather_message("Karachi", 30.5) == "The temperature in Karachi is 30.5 C."


def test_weather_message_handles_whole_number() -> None:
    """weather_message should show a whole-number temperature with a decimal point."""
    assert weather_message("Lahore", 25.0) == "The temperature in Lahore is 25.0 C."


def test_get_api_key_returns_value_when_set(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_api_key should return the key when the environment variable is set."""
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test-key-123")
    assert get_api_key() == "test-key-123"


def test_get_api_key_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_api_key should raise an error when the key is not set."""
    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
    with pytest.raises(ValueError):
        get_api_key()

def test_weather_message_with_fake_temperature() -> None:
    """weather_message ko fake temperature de kar message check karta hai."""
    assert weather_message("Lahore", 25.0) == "The temperature in Lahore is 25.0 C."

def test_parse_weather_response_extracts_city_and_temperature() -> None:
    """Fake API data se city aur temperature nikalne ka test."""
    from main import parse_weather_response

    data = {
        "name": "Lahore",
        "main": {"temp": 25.5}
    }

    assert parse_weather_response(data) == ("Lahore", 25.5)


def test_get_weather_uses_fake_api_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Fake response se get_weather ko test karta hai; internet call nahi hoti."""
    from unittest.mock import Mock
    from main import get_weather

    monkeypatch.setenv("OPENWEATHER_API_KEY", "fake-test-key")

    fake_response = Mock()
    fake_response.json.return_value = {
        "name": "Lahore",
        "main": {"temp": 25.5}
    }

    monkeypatch.setattr("main.requests.get", lambda *args, **kwargs: fake_response)

    assert get_weather("Lahore") == ("Lahore", 25.5)

def test_get_prayer_times_returns_five_prayers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Fake API response se paanch prayer timings check karta hai."""
    from unittest.mock import Mock
    from main import get_prayer_times

    fake_response = Mock()
    fake_response.json.return_value = {
        "data": {
            "timings": {
                "Fajr": "05:00",
                "Dhuhr": "12:15",
                "Asr": "15:45",
                "Maghrib": "18:00",
                "Isha": "19:30",
            }
        }
    }

    monkeypatch.setattr(
        "main.requests.get",
        lambda *args, **kwargs: fake_response,
    )

    result = get_prayer_times("Lahore")

    assert result == {
        "Fajr": "05:00",
        "Dhuhr": "12:15",
        "Asr": "15:45",
        "Maghrib": "18:00",
        "Isha": "19:30",
    }
