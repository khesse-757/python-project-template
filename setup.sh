#!/bin/bash
# Setup script for initializing a new project from this template

set -e

echo "Python Project Template Setup"
echo "=============================="
echo

read -p "Enter project name (e.g., my-awesome-project): " PROJECT_NAME
read -p "Enter package name (e.g., my_awesome_project): " PACKAGE_NAME
read -p "Enter your name: " AUTHOR_NAME
read -p "Enter your email: " AUTHOR_EMAIL
read -p "Enter your GitHub username: " GITHUB_USER
read -p "Enter project description: " DESCRIPTION

echo
echo "Updating project files..."

# Move template README to actual README
mv PROJECT_README.template README.md

# Update pyproject.toml
sed -i "s/project-name/$PROJECT_NAME/g" pyproject.toml
sed -i "s/project_name/$PACKAGE_NAME/g" pyproject.toml
sed -i "s/Your Name/$AUTHOR_NAME/g" pyproject.toml
sed -i "s/your.email@example.com/$AUTHOR_EMAIL/g" pyproject.toml
sed -i "s/yourusername/$GITHUB_USER/g" pyproject.toml
sed -i "s/A brief description of your project/$DESCRIPTION/g" pyproject.toml

# Update README.md
sed -i "s/Project Name/$PROJECT_NAME/g" README.md
sed -i "s/project-name/$PROJECT_NAME/g" README.md
sed -i "s/project_name/$PACKAGE_NAME/g" README.md
sed -i "s/yourusername/$GITHUB_USER/g" README.md

# Update LICENSE
sed -i "s/\[Your Name\]/$AUTHOR_NAME/g" LICENSE

# Update documentation
sed -i "s/Project Name/$PROJECT_NAME/g" docsrc/source/conf.py
sed -i "s/Your Name/$AUTHOR_NAME/g" docsrc/source/conf.py
sed -i "s/project-name/$PROJECT_NAME/g" docsrc/source/*.rst
sed -i "s/project_name/$PACKAGE_NAME/g" docsrc/source/*.rst
sed -i "s/yourusername/$GITHUB_USER/g" docsrc/source/*.rst

# Update Docker files
sed -i "s/project-name/$PROJECT_NAME/g" compose.yml
sed -i "s/project_name/$PACKAGE_NAME/g" docker/Dockerfile

# Rename src directory
if [ -d "src/project_name" ]; then
    mv src/project_name "src/$PACKAGE_NAME"
fi

# Update test files
sed -i "s/project_name/$PACKAGE_NAME/g" test/unit/*.py
sed -i "s/project_name/$PACKAGE_NAME/g" test/integration/*.py

echo "Done!"
echo
echo "Next steps:"
echo "1. Create virtual environment: python3 -m venv venv"
echo "2. Activate it: source venv/bin/activate"
echo "3. Install: make install"
echo "4. Run tests: make test"