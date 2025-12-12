"""
Unit tests for configuration module.
"""

import pytest

from project_name.config import Config


class TestConfig:
    """Test cases for Config class."""

    def test_default_config(self):
        """Test that default configuration is created correctly."""
        config = Config()
        assert isinstance(config.debug, bool)
        assert config.log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def test_set_config_values(self):
        """Test updating configuration values."""
        config = Config()
        config.set(debug=True, log_level="DEBUG")
        assert config.debug is True
        assert config.log_level == "DEBUG"

    def test_invalid_log_level_raises_error(self):
        """Test that invalid log level raises ValueError."""
        with pytest.raises(ValueError, match="Invalid log_level"):
            Config(log_level="INVALID")

    def test_set_invalid_attribute_raises_error(self):
        """Test that setting non-existent attribute raises AttributeError."""
        config = Config()
        with pytest.raises(AttributeError, match="Config has no attribute"):
            config.set(nonexistent="value")

    def test_log_level_case_insensitive(self):
        """Test that log level is case-insensitive."""
        config = Config(log_level="debug")
        assert config.log_level == "DEBUG"