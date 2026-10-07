import tomllib
from pathlib import Path

from plinth_reach import greet, version

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def test_greet() -> None:
    assert greet("world") == "Hello, world!"


def test_version_matches_pyproject() -> None:
    expected = tomllib.loads(PYPROJECT.read_text())["project"]["version"]
    assert version() == expected
