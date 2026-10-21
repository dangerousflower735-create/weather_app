"""Weather app ka pehla function."""

def greet_user(name: str) -> str:
    """User ko welcome message wapas karta hai."""
    return f"Assalam o Alaikum, {name}! Weather app mein khush aamdeed."


if __name__ == "__main__":
    print(greet_user("Shafaq"))
    print(greet_user("Ahmed"))