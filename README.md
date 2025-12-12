# Python Project Template

A clean, simple Python project template with modern tooling and CI/CD.

## What This Is

This is a template repository for starting new Python projects. It includes:

- Modern packaging with pyproject.toml
- Testing with pytest
- Code quality with ruff
- Documentation with Sphinx
- Docker support
- GitHub Actions for CI/CD
- Automatic releases when VERSION file changes

## How to Use

1. Clone or download this repository
2. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. Answer the prompts with your project details
4. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install:
   ```bash
   make install
   ```
6. Verify everything works:
   ```bash
   make test
   make lint
   ```

## What Gets Customized

The setup script will update:
- Project name and description
- Author information
- GitHub URLs
- Package name (renames src/project_name to your package)
- All file references

## Project Structure

```
python-template/
├── .github/workflows/    # CI/CD workflows
├── docker/              # Docker configuration
├── docsrc/source/       # Sphinx documentation
├── src/project_name/    # Your package code
├── test/               # Tests (unit and integration)
├── pyproject.toml      # Project configuration
├── VERSION             # Version tracking
└── setup.sh           # Initialization script
```

## After Setup

Once you've run setup.sh:

1. Initialize git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create GitHub repository and push:
   ```bash
   git remote add origin https://github.com/yourusername/your-project.git
   git branch -M main
   git push -u origin main
   ```

3. Add PyPI token to GitHub secrets for automatic publishing:
   - Go to repository Settings > Secrets > Actions
   - Add `PYPI_API_TOKEN` with your PyPI token

## Making Releases

To create a release:

1. Update the VERSION file
2. Commit and push to main
3. GitHub Actions will automatically:
   - Run tests
   - Build the package
   - Create a GitHub release
   - Publish to PyPI

## Requirements

- Python 3.11 or higher
- pip
- git

## License

MIT License - use this template for anything you want.