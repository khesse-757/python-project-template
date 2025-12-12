# Contributing

Thanks for considering contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch for your feature
4. Make your changes
5. Run tests
6. Submit a pull request

## Development Setup

```bash
git clone https://github.com/yourusername/project-name.git
cd project-name
python3 -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

## Running Tests

```bash
# All tests
pytest

# Unit tests only
pytest test/unit

# With coverage
pytest --cov=src
```

## Code Quality

```bash
# Check code
ruff check .

# Auto-fix issues
ruff check --fix .
```

## Commit Messages

Use clear, descriptive commit messages. Example:

```
Add user authentication feature

- Implement JWT token generation
- Add login endpoint
- Update documentation
```

## Questions

Open an issue if you have questions or need help.