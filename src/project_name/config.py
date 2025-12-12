"""
Configuration management for the project.
"""

import os
from dataclasses import dataclass, field


@dataclass
class Config:
    """
    Application configuration.

    Attributes:
        debug: Enable debug mode
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        data_dir: Directory for data files
    """

    debug: bool = field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    data_dir: str | None = field(default_factory=lambda: os.getenv("DATA_DIR"))

    def __post_init__(self):
        """Validate configuration after initialization."""
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.log_level.upper() not in valid_log_levels:
            raise ValueError(
                f"Invalid log_level: {self.log_level}. "
                f"Must be one of {valid_log_levels}"
            )
        self.log_level = self.log_level.upper()

    def set(self, **kwargs):
        """
        Update configuration values.

        Args:
            **kwargs: Configuration key-value pairs to update

        Example:
            >>> config.set(debug=True, log_level="DEBUG")
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Config has no attribute '{key}'")

        # Re-run validation
        self.__post_init__()


# Global configuration instance
config = Config()