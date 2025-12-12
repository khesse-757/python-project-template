"""
Project Name - A brief description of your project.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("project-name")
except PackageNotFoundError:
    __version__ = "0.0.0.dev"

__all__ = ["__version__"]