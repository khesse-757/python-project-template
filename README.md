# Python Project Template

A clean, modern Python project template with testing, documentation, and CI/CD.

## What's Included

* Modern packaging with pyproject.toml
* Testing with pytest
* Code quality with ruff
* Documentation with Sphinx
* Docker support
* GitHub Actions CI/CD
* Automatic releases when VERSION changes

## Quick Start

1. Clone this template:
   ```bash
   git clone git@github.com:khesse-757/python-project-template.git my-project
   cd my-project
   rm -rf .git
   ```

2. Run setup:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .[dev]
   ```

4. Verify:
   ```bash
   pytest
   ruff check .
   make docs
   ```

## Project Structure

```
project/
├── .github/workflows/    # CI/CD workflows
├── docker/              # Docker configuration
├── docsrc/source/       # Sphinx documentation
├── src/package_name/    # Your code
├── test/               # Tests
├── pyproject.toml      # Project configuration
├── VERSION             # Version tracking
└── Makefile           # Common tasks
```

## Features

### Testing

* pytest for unit and integration tests
* Code coverage tracking
* Automated testing on push/PR

### Documentation

* Sphinx with Read the Docs theme
* Auto-generated API docs
* Two deployment options (see DOCUMENTATION_DEPLOYMENT.md)

### CI/CD

* Automated testing on GitHub Actions
* Automatic releases when VERSION is updated
* Optional PyPI publishing
* Cross-platform testing (Ubuntu, macOS, Windows)

### Code Quality

* Ruff for linting and formatting
* Pre-configured sensible defaults
* Automatic checks in CI

### Docker

* Ready-to-use Dockerfile
* Docker Compose configuration
* Development and production setups

## Usage

### Common Commands

```bash
make install       # Install with dev dependencies
make test         # Run all tests
make lint         # Check code quality
make format       # Format code
make docs         # Build documentation
```

### Making Releases

1. Update VERSION file:
   ```bash
   echo "1.2.3" > VERSION
   ```

2. Commit and push to main:
   ```bash
   git commit -am "Release v1.2.3"
   git push origin main
   ```

3. GitHub Actions automatically:
   * Runs tests
   * Builds package
   * Creates GitHub release
   * Publishes to PyPI (if configured)

### Documentation

See [DOCUMENTATION_DEPLOYMENT.md](DOCUMENTATION_DEPLOYMENT.md) for detailed documentation setup options:

* **Option 1:** GitHub Pages (gh-pages branch) - Standard approach
* **Option 2:** In-repo docs folder - For sites with separate content

## Customization

### First Steps

1. Update pyproject.toml with your project details
2. Rename src/project_name to your package name
3. Update documentation in docsrc/source/
4. Add your dependencies to pyproject.toml

### Optional: PyPI Publishing

By default, the release workflow does NOT publish to PyPI. To enable:

1. Uncomment PyPI section in `.github/workflows/release.yml`
2. Add PYPI_API_TOKEN to GitHub secrets

### Optional: Custom Domain

For documentation with custom domain:

1. Add CNAME file to docsrc/source/
2. Configure DNS
3. See DOCUMENTATION_DEPLOYMENT.md

## Requirements

* Python 3.11+
* pip
* git

## License

MIT License - use this template however you want.