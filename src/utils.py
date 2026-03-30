"""Utility functions."""
import json
import csv
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"


def load_config():
    return {
        "app_name": "test-app",
        "version": "1.0.0",
        "debug": False,
    }


def read_json(filename):
    with open(DATA_DIR / filename) as f:
        return json.load(f)


def read_csv(filename):
    with open(DATA_DIR / filename) as f:
        return list(csv.DictReader(f))


def format_currency(amount):
    return f"${amount:,.2f}"
