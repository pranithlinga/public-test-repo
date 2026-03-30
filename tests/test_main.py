"""Tests for main module."""
import pytest
from src.main import main


def test_main_runs():
    # Smoke test
    main()


def test_main_loads_data():
    from src.models.user import User
    users = User.load_all()
    assert len(users) > 0
