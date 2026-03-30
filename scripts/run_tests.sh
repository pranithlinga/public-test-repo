#!/bin/bash
set -e
echo "Running tests..."
python -m pytest tests/ -v
echo "All tests passed."
