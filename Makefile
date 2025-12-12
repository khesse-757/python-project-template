.PHONY: help install test lint format docs clean

help:
	@echo "Available commands:"
	@echo "  make install    - Install package with dev dependencies"
	@echo "  make test       - Run all tests"
	@echo "  make lint       - Check code quality"
	@echo "  make format     - Format code"
	@echo "  make docs       - Build documentation"
	@echo "  make clean      - Remove build artifacts"

install:
	pip install -e .[dev]

test:
	pytest -v

lint:
	ruff check .

format:
	ruff check --fix .
	ruff format .

docs:
	sphinx-build -b html docsrc/source build/docs

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +