"""Entry point: `python -m <package>`. Wires settings and logging together."""

import logging

from .log import setup_logging
from .settings import get_settings

logger = logging.getLogger(__name__)


def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)
    logger.info("Started (log level: %s)", settings.log_level)


if __name__ == "__main__":
    main()
