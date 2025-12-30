import logging

from insinoorilaskin.logger import ROOT_LOGGER_NAME, setup_logging

logger = logging.getLogger(ROOT_LOGGER_NAME)


def main() -> None:
    setup_logging()

if __name__ == "__main__":
    main()
