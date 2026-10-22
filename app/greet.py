def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {nam}!"


def shout(name: str = "World") -> str:
    """Return the greeting in upper case."""
    return greet(name).upper()
