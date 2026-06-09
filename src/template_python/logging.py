"""
Logging utilities.

Side effects:
Automatically configures basic logging via `setup_logging()` on import.
"""

import logging

from src.template_python.utils import get_env

_LOGGING_CONFIGURED = False


def setup_logging(level: str | int | None = None):
    """Configure root logging."""
    global _LOGGING_CONFIGURED
    if _LOGGING_CONFIGURED:
        return

    if level is None:
        if get_env("DEBUG") is not None:
            level = "DEBUG" if get_env("DEBUG", cast=bool) else "INFO"
        else:
            level = "INFO"

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    _LOGGING_CONFIGURED = True


def get_logger(name: str | None = None) -> logging.Logger:
    """Get a logger, ensuring logging is configured at least minimally."""
    if not _LOGGING_CONFIGURED:
        setup_logging()  # fallback default
    return logging.getLogger(name)


def set_global_log_level(level: str):
    """Change the log level of all existing loggers."""
    lvl = getattr(logging, level.upper(), None)
    if not isinstance(lvl, int):
        raise ValueError(f"Invalid log level: {level}")
    logging.getLogger().setLevel(lvl)
    for name in list(logging.root.manager.loggerDict):
        logging.getLogger(name).setLevel(lvl)


# --- Auto-initialize at import time
if not _LOGGING_CONFIGURED:
    setup_logging()
