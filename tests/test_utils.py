"""Tests for utility functions."""
import pytest
from src.utils import load_config, format_currency


def test_load_config():
    config = load_config()
    assert "app_name" in config
    assert config["version"] == "1.0.0"


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0) == "$0.00"
