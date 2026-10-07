"""The application package."""

from importlib.metadata import version as _distribution_version


def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


def version() -> str:
    """Return the installed version of this package."""
    return _distribution_version("plinth_reach")
