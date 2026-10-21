"""Tests for the weather app's main module."""

import pytest
from main import get_api_key, greet_user, weather_message


def test_greet_user_returns_welcome_message() -> None:
    """greet_user should return a welcome line with the name."""
    assert greet_user("Shafaq") == "Welcome, Shafaq!"


def test_weather_message_formats_temperature() -> None:
    """weather_message should show city and temperature in one line."""
    assert weather_message("Karachi", 30.5) == "The temperature in Karachi is 30.5 C."


def test_get_api_key_returns_value_when_set(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_api_key should return the key when the environment variable is set."""
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test-key-123")
    assert get_api_key() == "test-key-123"


def test_get_api_key_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_api_key should raise a clear error when the key is not set."""
    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
    with pytest.raises(ValueError):
        get_api_key()
