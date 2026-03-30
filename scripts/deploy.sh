#!/bin/bash
set -e
echo "Deploying application..."
pip install -r requirements.txt
python -m pytest tests/
echo "Tests passed. Deploying..."
echo "Deployment complete."
