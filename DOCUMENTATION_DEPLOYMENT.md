# Documentation Deployment Guide

This template includes Sphinx documentation setup. You have two deployment options.

## Option 1: GitHub Pages (gh-pages branch)

Best for: Standard Python packages where docs are the main GitHub Pages content.

### Setup

1. Documentation workflow is already configured in `.github/workflows/docs.yml`
2. Enable GitHub Pages:
   - Go to repo Settings > Pages
   - Source: Deploy from a branch
   - Branch: gh-pages / root
   - Save
3. Push changes to trigger workflow
4. Docs will be at: `https://yourusername.github.io/your-repo/`

### Custom Domain

Add CNAME file to `docsrc/source/`:
```
docs.yourdomain.com
```

Configure DNS to point to `yourusername.github.io`

## Option 2: In-Repo docs/ Folder

Best for: Projects with a separate website (like PyScript apps) that want docs at `/docs/`

### Setup

1. Update `.github/workflows/docs.yml` to build to `docs/` instead of gh-pages
2. Update `.gitignore` to NOT ignore the `docs/` directory
3. Add `.nojekyll` to repo root
4. Build docs locally first:
   ```bash
   sphinx-build -b html docsrc/source docs
   ```
5. Commit the docs folder:
   ```bash
   git add docs/
   git commit -m "Add documentation"
   git push
   ```
6. Docs will be at: `https://yoursite.com/docs/`

### Workflow for Option 2

Replace `.github/workflows/docs.yml` with:

```yaml
name: Documentation

on:
  push:
    branches:
      - main
    paths:
      - 'docsrc/**'
      - 'src/**'

permissions:
  contents: write

jobs:
  docs:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]

    - name: Build documentation
      run: |
        sphinx-build -b html docsrc/source docs

    - name: Commit documentation
      run: |
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git add docs/
        git diff --staged --quiet || git commit -m "Update documentation"
        git push
```

Update `.gitignore`:
```
# Sphinx documentation
docsrc/_build/

# Note: docs/ is NOT ignored for Option 2
```

Add `.nojekyll` to root:
```bash
touch .nojekyll
```

## Local Testing

Before deploying, always test locally:

```bash
# Build docs
sphinx-build -b html docsrc/source build/docs

# Or use make
make docs

# Serve locally
cd build/docs  # or cd docs for Option 2
python3 -m http.server 8001

# Open http://localhost:8001
```

## Customizing Documentation

Edit files in `docsrc/source/`:
- `index.rst` - Main documentation page
- `installation.rst` - Installation instructions
- `usage.rst` - Usage examples
- `api.rst` - API reference

Update `conf.py` for project-specific settings:
- Project name
- Author
- Theme settings

## Building Locally

```bash
# Clean previous builds
rm -rf build/docs docs/

# Build fresh
sphinx-build -b html docsrc/source build/docs
```

## Troubleshooting

**Docs look unstyled on GitHub Pages:**
- Add `.nojekyll` file to repo root
- Wait 2-3 minutes for GitHub to redeploy

**Docs not updating:**
- Check GitHub Actions tab for workflow errors
- Verify workflow has write permissions
- Check that paths in workflow match your changes

**Local build errors:**
- Install dev dependencies: `pip install -e .[dev]`
- Check for syntax errors in .rst files
- Verify all files referenced in toctree exist