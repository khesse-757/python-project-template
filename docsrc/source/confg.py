# Sphinx configuration file

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Project Name'
copyright = '2025, Your Name'
author = 'Your Name'

with open('../../VERSION') as f:
    release = f.read().strip()
version = '.'.join(release.split('.')[:2])

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

napoleon_google_docstring = True
napoleon_numpy_docstring = True