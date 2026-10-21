
"""main.py ke functions ke liye tests."""

from main import greet_user, weather_message


def test_greet_user_contains_name() -> None:
    """greet_user message mein user ka naam hona chahiye."""
    assert "Shafaq" in greet_user("Shafaq")


def test_weather_message_contains_city() -> None:
    """weather_message message mein shehar ka naam hona chahiye."""
    assert "Lahore" in weather_message("Shafaq", "Lahore")
