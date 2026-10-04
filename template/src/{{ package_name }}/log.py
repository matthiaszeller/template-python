"""
Logging setup.

Call `setup_logging()` once, at your application's entry point. Modules should not configure logging;
they just use `logging.getLogger(__name__)`.
"""

import logging


def setup_logging(level: int | str = "INFO") -> None:
    """Configure root logging. Safe to call again to change the level."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        force=True,
    )
