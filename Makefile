.PHONY: test lint run seed

test:
	python -m pytest tests/ -v

run:
	python src/main.py

seed:
	python scripts/seed_db.py

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
