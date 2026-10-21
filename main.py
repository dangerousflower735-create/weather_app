
"""Weather app ka pehla function."""

def greet_user(name: str) -> str:
    """User ko welcome message wapas karta hai."""
    return f"Assalam o Alaikum, {name}! Weather app mein khush aamdeed."


def weather_message(name: str, city: str) -> str:
    """User ke naam aur shehar ke saath mausam ka pehla message banata hai."""
    return f"{name}, {city} ka mausam jaan'ne ke liye tayyar ho jaiye."


if __name__ == "__main__":
    print(greet_user("Shafaq"))
    print(weather_message("Shafaq", "Lahore"))
