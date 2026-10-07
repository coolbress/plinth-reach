import tomllib
from pathlib import Path

import pytest

import plinth_reach
from plinth_reach import greet, version

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def test_greet() -> None:
    assert greet("world") == "Hello, world!"


def test_version_matches_pyproject(monkeypatch: pytest.MonkeyPatch) -> None:
    # Installed metadata goes stale when pyproject changes without a reinstall,
    # so check that version() asks for this project's distribution instead.
    name = tomllib.loads(PYPROJECT.read_text())["project"]["name"]
    monkeypatch.setattr(plinth_reach, "_distribution_version", lambda dist: f"{dist}!")
    assert version() == f"{name}!"
